import json
from flask import Flask, request, redirect, url_for, render_template
import re

app = Flask(__name__)
@app.route('/') #por defeito isto é um pedido GET
def hello_world():
    #return '<p>Hello World!</p>'
    return render_template("home.html")


db_file=open('conceitos_backup.json', "r", encoding="utf-8")
db=json.load(db_file)
db_file.close()
@app.route('/api/conceitos')
def conceitos():
    return (db)


@app.route('/api/conceitos/<designacao>')
def api_conceito(designacao):
    return {"designacao":f'{designacao}', "descricao":db[designacao]}


@app.route('/conceitos')
def adiciona_conceito():
    #por json
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Designações")

@app.route('/conceitos/<designacao>')
def api_conceito_designacao(designacao):
    if designacao in db:
        return render_template("conceito_descricao.html", designacao=designacao, descricao=db[designacao], title="Conceito e desginação")
    else:
        return render_template("conceito_descricao.html", designacao="Not Found", descricao="Not Found",
                               title="Conceito e desginação")


@app.post("/conceitos")
def adiciona_conceito_novo():
    designacao = request.form.get('designacao')
    #print(designacao)
    descricao = request.form.get('descricao')
    db[designacao] = descricao  # adiciona À base de dados json uma nova chave que corresponde à descrição, e o valor é a designação

    f_out = open("conceitos.json", "w", encoding="utf-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    designacoes= db.keys()
    #print(designacoes)
    return render_template("conceitos.html", designacoes=designacoes, title="Conceitos")


@app.route('/pesquisar', methods=['GET', 'POST'])
def pesquisar_page():
    resultados = []
    termo = request.form.get("termo", "").strip().lower()  # Captura o termo
    exact_match = request.form.get("exact_match")  # Retorna "on" se marcada, None se não marcada

    if termo:
        if exact_match:  # Pesquisa exata ativada
            regex = re.compile(rf'\b{termo}\b', re.IGNORECASE)
        else:  # Pesquisa por qualquer ocorrência do termo
            regex = re.compile(rf'{termo}', re.IGNORECASE)

        for designacao, descricao in db.items():
            if regex.search(designacao) or regex.search(descricao):
                designacao = regex.sub(lambda m: f"<b>{m.group(0)}</b>", designacao)
                descricao = regex.sub(lambda m: f"<b>{m.group(0)}</b>", descricao)
                resultados.append(f"{designacao}: {descricao}")

    return render_template("pesquisar.html", title="Pesquisar", resultados=resultados, termo=termo, exact_match=exact_match)

def gera_termo_bold(matched, termo):
    #print(matched)
    palavra = matched.group(0).strip().lower()
    print(f"Palavra: {palavra}")
    print(f"termo: {termo}")
    if palavra == termo:
        print("Sucesso")
        #return f"<a href='#' target='_blank' title='{conceitos[titulo]}'>{titulo}</a>" #vai buscar aos conceitos a definição do titulo
        return f"<b>{palavra}</b>"
    else:
        return f"{palavra}"





app.run(host="localhost",port=4002,debug=True)



