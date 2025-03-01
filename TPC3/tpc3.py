import re


# Abrir e ler o conteúdo do ficheiro
with open("dic_med.txt", "r", encoding="utf-8") as file:
    texto = file.read()

with open("dic_original.txt", "w", encoding="utf-8") as file_dic:
    file_dic.write(repr(texto))
    file_dic.close()

#Tratamento das descrições
texto = re.sub(r'\n{1,2}\f([a-zA-ZÀ-ÖØ-öø-ÿ|\d]+(.+\n?.+){1,2}\.\n)',r'\g<1>',texto)

#existem descrições que tinham antes de si entre 1 a 2 quebras de linha e uma quebra de página, isto permite eliminar estas quebras,
#Para se determinar que o texto é uma descrição e não uma designação é pelo facto de o texto
#terminar num ponto final seguido de uma quebra de linha. O grupo de captura permite guardar apenas a descrição sem as quebras iniciais,
#o que é importante para o passo seguinte onde se marca designações, não se marcar descrições acidentalmente



#retirar as quebras de página do texto
texto=re.sub(r"\f","",texto, 0)

#marcar as designações
texto=re.sub(r"\n\n","\n\n@",texto, 0)

def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub("\n", " ",descricao)
    return descricao

#separa os conceitos através da marcação feita previamente
conceitos_raw=re.findall(r"@(.*)\n([^@]*)",texto)

#Cria tuplos com a designação e a respetiva descrição "limpa" dos \n
conceitos=[(designacao,limpa_descricao(descricao)) for designacao,descricao in conceitos_raw]


def gera_html(conceitos):

    html_header=f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Dicionário</title>
    </head>
    <body>
    <h1>Dicionário de Conceitos Médicos</h1>'''
    html_conceitos=''''''

    for designacao, descricao in conceitos:
        html_conceitos+= f""" 
        <div>
            <h2>{designacao}:</h2>
            <p>{descricao}</p>
            <hr/>
        </div>
        """


    html_footer='''    
        </body>
    </html>
    '''

    return html_header+html_conceitos+html_footer

html=gera_html(conceitos)
with open("dic2.html", "w", encoding="utf-8") as file_dic:
    file_dic.write(html)
    file_dic.close()


file.close()