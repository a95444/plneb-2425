# TPC5 - André Sousa - PG52564

## Introdução
Foram implementadas duas rotas para a exibição de conceitos armazenados numa base de dados JSON. Estas rotas permitem listar todas as designações disponíveis e exibir a descrição detalhada de um conceito específico.

## Rota Listagem de Conceitos
Esta rota permite listar todas as designações de conceitos armazenados na base de dados e apresenta-las na página `conceitos.html`.

Cada designação na página `conceitos.html` é exibida como um link clicável que direciona para a rota que apresenta detalhes do conceito selecionado. Isto é feito através da função `url_for`, que gera dinamicamente a URL correspondente para cada conceito:

```html
<ul>
    {% for designacao in designacoes %}
        <li>
            <a href="{{ url_for('api_conceito_designacao', designacao=designacao) }}">
                {{designacao}}
            </a>
        </li>
    {% endfor %}
</ul>
```

Aqui, `url_for('api_conceito_designacao', designacao=designacao)` gera a URL correta para a rota que apresenta a descrição do conceito selecionado.

## Rota Descrição de um Conceito
A segunda rota permite visualizar a descrição de um conceito específico. Quando um utilizador clica num dos links gerados na página `conceitos.html`, é redirecionado para esta rota, que renderiza a página `conceito_descricao.html`. Esta página exibe a designação e a descrição do conceito correspondente. Para isso foi criado o seguinte:

```python
@app.route('/conceitos/<designacao>')
def api_conceito_designacao(designacao):
    return render_template("conceito_descricao.html", designacao=designacao, descricao=db[designacao], title="Conceito e desginação")

```
## Template `conceito_descricao.html`
Foi necessário criar a página `conceito_descricao.html` para apresentar os detalhes do conceito selecionado. Esta página recebe a designação e a descrição do conceito e exibe-as num formato organizado.

