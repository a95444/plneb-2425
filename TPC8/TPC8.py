from bs4 import BeautifulSoup
import requests
import json

url = "https://www.atlasdasaude.pt/doencasaaz/"
url_base = "https://www.atlasdasaude.pt/"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

doencas = {}

def adquirir_letras():
    contador=0

    for letter in soup.find_all("div", class_="views-summary views-summary-unformatted"):
        contador+=1
        if contador==0:
            return
        else:
            letra = letter.text.strip().lower()
            print(letra)
            extrair_desc_desig(letra)

def doenca_info(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    div_content = soup.find("div", class_="node-doencas")
    if not div_content:
        return {}

    info = {
        "info_clinica": "",
        "causas": "",
        "sintomas": ["",[]],
        "diagnostico": "",
        "tratamento": "",
        "artigos_relacionados": {},
        "nota": "",
        "site": "",
    }

    # Extrair o corpo principal do conteúdo
    body_div = div_content.find("div", class_="field-name-body")
    if not body_div:
        return info

    field_item = body_div.find("div", class_="field-item even")
    if not field_item:
        return info

    # Extrair a nota
    nota_div = div_content.find("div", class_="field-name-field-nota")
    if not nota_div:
        pass
    else:
        field_item_nota = nota_div.find("div", class_="field-item even")
        if not field_item_nota:
            pass
        else:
            nota_content = field_item_nota.get_text(strip=True)
            info["nota"] = nota_content

        # Extrair o site
        site_div = div_content.find("div", class_="field-name-field-site")
        #print(f"NOTA DIV: {site_div}")
        if not site_div:
            pass
        else:
            field_item_site = site_div.find("div", class_="field-item even")

            if not field_item_site:
                pass
            else:
                site_content = field_item_site.get_text(strip=True)

                info["site"] = site_content



    # Coletar info_clinica (tudo antes do primeiro h2)
    info_clinica_parts = []
    for element in field_item.children:
        if element.name == 'h2': #quando encontrar um titulo, para o ciclo pois já não se está na secção inicial
            break
        if element.name == 'p':
            info_clinica_parts.append(element.get_text(strip=True)) #captar o texto inicial da doença
    info["info_clinica"] = ' '.join(info_clinica_parts).strip()

    # Processar cada seção h2
    h2_tags = field_item.find_all('h2')
    for h2 in h2_tags:
        section_title = h2.get_text(strip=True).lower()
        next_elements = []
        next_sibling = h2.find_next_sibling()
        while next_sibling and next_sibling.name != 'h2':
            next_elements.append(next_sibling)
            next_sibling = next_sibling.find_next_sibling()

        # Determinar a seção com base no título
        if 'causas' in section_title:
            causas = []
            for el in next_elements:
                if el.name == 'p':
                    causas.append(el.get_text(strip=True))
                elif el.name == 'ul':
                    causas.extend([li.get_text(strip=True) for li in el.find_all('li')])
            info["causas"] = ' '.join(causas).strip()
        elif 'sintomas' in section_title:
            #print(f"Next elements: {next_elements} ")
            sintomas=[]
            for el in next_elements:
                if el.name == 'p':
                    sintomas.append(el.get_text(strip=True))
                    #info["sintomas"][0].append(el.get_text(strip=True))
                if el.name == 'ul':
                    info["sintomas"][1].append([li.get_text(strip=True) for li in el.find_all('li')])
                info["sintomas"][0] = ' '.join(sintomas).strip()

        if ('diagnóstico'or'diagnostico') in section_title :
            diagnostico = []
            for el in next_elements:
                if el.name == 'p':
                    diagnostico.append(el.get_text(strip=True))
                elif el.name == 'ul':
                    diagnostico.extend([li.get_text(strip=True) for li in el.find_all('li')])
            info["diagnostico"] = ' '.join(diagnostico).strip()


        elif 'tratamento' in section_title:
            tratamento = []
            for el in next_elements:
                if el.name == 'p':
                    tratamento.append(el.get_text(strip=True))
            info["tratamento"] = ' '.join(tratamento).strip()
        elif 'artigos relacionados' in section_title:
            for el in next_elements:
                if el.name == 'h3':
                    a_tag = el.find('a')
                    if a_tag:
                        info["artigos_relacionados"][a_tag.get_text(strip=True)] = a_tag.get('href', '')

    return info

def extrair_desc_desig(letter):
    url_letra = url + str(letter)
    print(f"URL NOVO: {url_letra}")
    response = requests.get(url_letra)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    for elem in soup.find_all("div", class_="views-row"):
        designacao_div = elem.find("div", class_="views-field-title")
        designacao = designacao_div.text.strip()

        link_tag = designacao_div.find("a")
        href = link_tag["href"] if link_tag else None
        url_palavra = url_base + href

        print(f"A processar: {designacao}")
        conteudo_palavra = doenca_info(url_palavra)


        descricao_div = elem.find("div", class_="views-field-body")
        descricao = ""
        if descricao_div and descricao_div.div:
            if descricao_div.div.p:
                descricao = descricao_div.div.p.text.strip().replace("\n", " ")
            else:
                descricao = descricao_div.div.text.strip().replace("\n", " ")

        doencas[designacao] = {
            "resumo": descricao,
            "url": url_palavra,
            "info_clinica": conteudo_palavra.get("info_clinica", ""), #.get retorna algo se estiver presente do dicionário
            "causas": conteudo_palavra.get("causas", ""),
            "sintomas": conteudo_palavra.get("sintomas", []),
            "diagnostico": conteudo_palavra.get("diagnostico", ""),
            "tratamento": conteudo_palavra.get("tratamento", ""),
            "artigos_relacionados": conteudo_palavra.get("artigos_relacionados", {}),
            "nota": conteudo_palavra.get("nota",""),
            "site": conteudo_palavra.get("site", "")
        }

adquirir_letras()

print(doencas)
f_out = open("doencas.json", "w", encoding="utf-8")
json.dump(doencas, f_out, indent=4, ensure_ascii=False)
f_out.close()