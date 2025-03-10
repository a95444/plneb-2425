import json
from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)
@app.route('/') #por defeito isto é um pedido GET
def hello_world():
    return '<p>Hello World!</p>'


db_file=open('conceitos_backup.json', "r", encoding="utf-8")
db=json.load(db_file)
db_file.close()
@app.route('/api/conceitos')
def conceitos():
    return (db)


@app.route('/api/conceitos/<designacao>')
def api_conceito(designacao):
    return {"designacao":f'{designacao}', "descricao":db[designacao]}


'''@app.post('/conceitos')
def adiciona_conceito():
    #por json
    data = request.get_json()
    #{"designacao":"", "descricao":""}
    db[data['designacao']] = data['descricao'] #adiciona À base de dados json uma nova chave que corresponde à descrição, e o valor é a designação
    print(db[data['designacao']])
    f_out=open("conceitos_backup.json", "w", encoding="utf-8")
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    
    return data
'''
@app.route('/conceitos')
def adiciona_conceito():
    #por json
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Designações")

@app.route('/conceitos/<designacao>')
def api_conceito_designacao(designacao):
    return render_template("conceito_descricao.html", designacao=designacao, descricao=db[designacao], title="Conceito e desginação")


app.run(host="localhost",port=4002,debug=True)



