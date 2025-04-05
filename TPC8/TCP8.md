# TPC8 - PG52564

## Funções Principais

### 1. `adquirir_letras()`
**Objetivo:**  
- Varredura da página principal para identificar todos os elementos que contêm as letras do alfabeto, representando a categorização dos termos.
- Para cada letra encontrada, invoca a função `extrair_desc_desig(letra)`, que processa os termos associados aquela letra.

**Resumo do Funcionamento:**  
- A função percorre os elementos com a classe `views-summary views-summary-unformatted`.
- Para cada elemento, extrai a letra (convertida para minúsculas) e a passa para `extrair_desc_desig(letra)`.

---

### 2. `doenca_info(url)`
**Objetivo:**  
- Acessar a página individual de um termo (doença) e extrair informações detalhadas sobre o conteúdo clínico.
- Organizar os dados extraídos em um dicionário com chaves como:
  - **info_clinica:** Texto introdutório antes do primeiro título (`<h2>`).
  - **causas:** Informações sobre as causas, que podem incluir parágrafos e listas.
  - **sintomas:** Estruturados em uma parte textual e, se disponíveis, em listas de sintomas.
  - **diagnostico:** Detalhes sobre o diagnóstico da doença.
  - **tratamento:** Descrição do tratamento proposto.
  - **artigos_relacionados:** Links e títulos de artigos relacionados à doença.
  - **nota:** Notas adicionais, caso existam.
  - **site:** Indicação de sites relevantes.

**Resumo do Funcionamento:**  
- Realiza uma requisição à URL da página do termo e usa BeautifulSoup para processar o HTML.
- Localiza a div principal (`node-doencas`) e extrai as informações das seções correspondentes.
- Utiliza um loop para coletar o conteúdo antes do primeiro `<h2>` e processa as seções seguintes com base no título de cada `<h2>`.

---

### 3. `extrair_desc_desig(letter)`
**Objetivo:**  
- Para uma dada letra, acessar a página que lista os termos correspondentes e extrair para cada termo:
  - **Designação:** O nome do termo (doença).
  - **Resumo:** Um resumo curto extraído da listagem.
  - **URL detalhado:** O link para a página completa do termo.
- Chamar a função `doenca_info(url)` para obter informações detalhadas de cada termo.
- Organizar e armazenar todas as informações coletadas em um dicionário global (`doencas`).

**Resumo do Funcionamento:**  
- Constrói a URL específica para a letra, faz a requisição e processa o HTML resultante.
- Para cada elemento que representa um termo (identificado pela classe `views-row`):
  - Extrai a designação e o link contido na tag `<a>`.
  - Constrói a URL completa para a página do termo e chama `doenca_info(url)` para extrair detalhes.
  - Reúne o resumo e as informações detalhadas, armazenando-as no dicionário `doencas`.

---

## Armazenamento dos Dados

Ao final do processo, o dicionário `doencas` contém os dados extraídos para cada termo, organizados em uma estrutura clara e consistente. Esse dicionário é, então, gravado num ficheiro JSON (`doencas.json`) utilizando a codificação UTF-8, facilitando sua utilização em futuras análises ou integrações.

```python
with open("doencas.json", "w", encoding="utf-8") as f_out:
    json.dump(doencas, f_out, indent=4, ensure_ascii=False)
