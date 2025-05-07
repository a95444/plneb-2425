from cgitb import strong

from bs4 import BeautifulSoup
import requests
import json

url = "https://revista.spmi.pt/index.php/rpmi/issue/archive"

all_articles = []

def get_archives():
    links_archives={}
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    contador=0
    for archive in soup.find_all("a", class_="title"):
        link = archive.get("href")
        titulo_archive=archive.get_text(strip=True)
        links_archives[titulo_archive]=link
        contador+=1
        if contador==3:
            return links_archives

def iterador():
    urls_archives=get_archives()
    for archive_title in urls_archives.keys():
        response = requests.get(urls_archives[archive_title])
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        articles = soup.find_all("div", class_="obj_article_summary")
        for article in articles:
            # Título e link do artigo
            title_tag = article.find("h3", class_="title").find("a")
            article_url = title_tag.get("href")
            info = extrair_info(article_url)
            info["archive"] = archive_title
            all_articles.append(info)




def extrair_info(url_article):
    response = requests.get(url_article)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    #keywords
    keywords_raw = soup.find("section", class_="item keywords").find("span").get_text()
    keywords = [kw.strip() for kw in keywords_raw.split(",") if kw.strip()]

    #Abstract
    abstract_dic={}
    abstract_section = soup.find("section", class_="item abstract")
    if abstract_section is None:
        # Se não existir secção de abstract retorna dicionário vazio
        pass
    else:
        for paragraph in abstract_section.find_all("p"):
            strong = paragraph.find("strong")
            if not strong:
                continue
            title = strong.get_text(strip=True).rstrip(':')
            strong.extract() #remove a tag <strong>
            texto= paragraph.get_text()
            abstract_dic[title] = texto

    #DOI
    doi_raw = soup.find("section", class_="item doi")
    doi_content = doi_raw.find("a").get("href")

    #PUBLISHDATE
    publishdate_raw= soup.find("div", class_="item published")
    publish_date= publishdate_raw.find("span").get_text()

    article_info = {
        "url":url_article,
        "keywords": keywords,
        "abstract": abstract_dic,
        "doi": doi_content,
        "publish_date": publish_date
    }
    #print(article_info)

    return article_info


iterador()

with open("articles.json", "w", encoding="utf-8") as f:
    json.dump(all_articles, f, indent=4, ensure_ascii=False)

print(f"{len(all_articles)} artigos gravados em articles.json")
