# TPC7 - PG52564

## 1. Implementação da Tabela com DataTables

A tabela interativa foi implementada utilizando a biblioteca [DataTables](https://datatables.net/), que simplifica a criação de tabelas dinâmicas e pesquisáveis.

- No template `tabela.html`, a tabela foi criada através do Jinja para iterar sobre um dicionário contendo as designações e descrições:

```html
<table id="tabela_conceitos" class="display">
    <thead>
        <tr>
            <th>Designação</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        {% for designacao, descricao in db.items() %}
            <tr>
                <td>{{ designacao }}</td>
                <td>{{ descricao }}</td>
            </tr>
        {% endfor %}
    </tbody>
</table>
```

- O JavaScript que inicializa o DataTables e habilita a pesquisa com expressões regulares está implementado no ficheiro criado para conter o conteúdo de JavaScript do código: `conceito_descricao.js`:

```javascript
$(document).ready(function() {
    $('#tabela_conceitos').DataTable({
        search: {
            regex: true
        }
    });
});
```

- A rota `@app.get("/conceitos/tabela")` no `tp7.py` renderiza o template `tabela.html`, passando o dicionário com as designações e respetivas descrições como argumento (db=db):

```python
@app.get("/conceitos/tabela")
def conceitos_tabela():
    return render_template("tabela.html", db=db, title="Tabela de Conceitos")
```

## 2. Adição da Página da Tabela à Home

Para tornar a página acessível a partir da Home, foi adicionado um botão na página `home.html`:

```html
<a href="/conceitos/tabela" class="btn btn-outline-secondary btn-lg px-4">Tabela de Conceitos</a>
```

Além disso, a opção também foi incluída no menu de navegação do `layout.html`:

```html
<li class="nav-item">
    <a class="nav-link" href="/conceitos/tabela">Tabela de Conceitos</a>
</li>
```

## 3. Estilização da Tabela

A tabela foi estilizada utilizando o CSS próprio do DataTables, importado no `layout.html`:

```html
<link rel="stylesheet" href="https://cdn.datatables.net/2.2.2/css/dataTables.dataTables.css" />
```

Adicionalmente, um CSS personalizado foi criado no arquivo `table.css` e importado no `tabela.html`:

```html
<link rel="stylesheet" href="/static/css/table.css">
```

Exemplo de alguns dos estilos aplicados:

```css
/* Ajusta espaçamento da tabela */
.container {
    max-width: 80%;
    margin: auto;
}

/* Centraliza a barra de pesquisa */
.dataTables_filter {
    text-align: center !important;
    margin-bottom: 10px;
}

/* Posiciona a paginação no canto inferior direito */
.dataTables_paginate {
    text-align: right !important;
    margin-top: 10px;
}
```

## 4. Pesquisa com Expressões Regulares

Para permitir a pesquisa usando expressões regulares, foi adicionada a opção `search.regex: true` na inicialização do DataTables:

```javascript
$(document).ready(function() {
    $('#tabela_conceitos').DataTable({
        search: {
            regex: true
        }
    });
});
```

---

