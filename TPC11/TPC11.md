# TPC11 - PG52564

## Objetivo

* Navegar pelos arquivos de edições e recolher os URLs destes.
* Aceder a cada edição e aceder aos artigos nela publicados.
* Para cada artigo, extraiu-se os seguintes campos:

  * URL do artigo
  * Keywords
  * Abstract, dividido por secções (Introdução, Métodos, Resultados, Conclusão)
  * DOI
  * Data de publicação
  * Edição de origem (`archive`)
* Consolidar todos os registos num único ficheiro JSON.

## Funcionamento

1. **Coleta de Edições**
   A função `get_archives()` acede ao arquivo de edições, varre os primeiros três links (`<a class="title">`), apenas para limitar o tempo de execução do código, já que poderia varrer todas as edições/archives, e devolve um dicionário com título da edição (já limpo de espaços/brancos) como chave e URL como valor.

2. **Iteração por Edições e Artigos**
   A função `iterador()` percorre cada edição obtida, acede à página da edição, identifica todas as `<div class="obj_article_summary">` e extrai o link de cada artigo. Para cada URL, chama `extrair_info()` e guarda o resultado numa lista global.

3. **Extração de Metadados de Artigo**
   A função `extrair_info(url_article)` faz o download da página de artigo e monta um dicionário com:

   * **keywords**: texto de `<section class="item keywords">` dividido por vírgulas e limpo.
   * **abstract**: cada parágrafo `<p>` que inicia com `<strong>` dá origem a uma entrada do dicionário (`{"Introdução": "…", "Métodos": "…"}`).
   * **doi**: URL de DOI em `<section class="item doi"><a href="…">`.
   * **publish\_date**: texto em `<div class="item published"><span>…</span>`.
   * **archive**: título da edição, adicionada pelo `iterador()`.

4. **Gerar JSON**
   No final, toda a lista de dicionários é escrita em `articles.json` com indentação e codificação UTF‑8, para consumo posterior.

## Estrutura do Ficheiro JSON

O resultado é uma lista de objetos, por exemplo:

```json
[
  {
    "url": "https://revista.spmi.pt/index.php/rpmi/article/view/2579",
    "keywords": ["Mortalidade", "Velocidade de Sedimentação"],
    "abstract": {
      "Introdução": "O nosso objetivo foi estudar a associação …",
      "Métodos": "Estudo retrospetivo de todos os doentes …",
      "Resultados": "Uma VS superior a 100 mm/h …",
      "Conclusão": "Verificámos que quase todos os doentes …"
    },
    "doi": "https://doi.org/10.24950/rspmi.2579",
    "publish_date": "2025-03-31",
    "archive": "Janeiro / Março"
  }
]
```

Cada objeto inclui informação completa que permite filtrar e analisar artigos por tema, data e contexto de publicação.
