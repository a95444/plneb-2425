# TPC6 - André Sousa - PG52564

## Estrutura da página `pesquisar.html`

A página `pesquisar.html` é responsável por permitir a pesquisa de um termo no dicionário de termos desenvolvido nas aulas anteriores. A estrutura deste inclui:

- Um campo de entrada (`input`) onde o utilizador pode inserir o termo desejado;
- Uma *checkbox* chamada Pesquisa Exata, que permite escolher entre uma procura exata ou por qualquer ocorrência do termo.
- Um botão de submissão para efetuar a pesquisa.
- Exibição dos resultados dentro de uma lista, com o termo pesquisado destacado a negrito.

Se a pesquisa não encontrar resultados, exibe uma mensagem a informar que nada foi encontrado.

---

## Explicação da função `pesquisar_page()`

A função `pesquisar_page()` trata a lógica de busca e exibição dos resultados. A sua respetiva estrutura é:

1. Recebe o termo de pesquisa do formulário como argumento e converte-o para minúsculas.
2. Verifica se a *checkbox* de "Pesquisa Exata" está marcada:
   - Em caso positivo, utiliza uma expressão regular que procura a palavra inteira (`\b{termo}\b`).
   - Caso contrário, busca qualquer ocorrência do termo inserido (`{termo}`), podendo este encontrar-se no meio de uma palavra.
3. Percorre a base de dados (`db.items()`) e verifica se o termo está presente quer na designação, quer na descrição.
4. Se houver correspondências, utiliza o comando `regex.sub()` para substituir as ocorrências do termo por uma versão deste a negrito (`<b>termo</b>`).
5. Adiciona as ocorrências a negrito a uma lista e faz a renderização novamente da página `pesquisar.html`, passando os resultados e o termo pesquisado como dados.

---

## Explicação da função `gera_termo_bold()`

Esta função desenvolvida numa aula anterior foi reutilizada para formatar as correspondências, substituindo o termo pesquisado por uma versão deste a negrito.&#x20;

1. Recebe um objeto `match` que contêm uma palavra da descrição ou da designação, dependendo de onde foi detetada a ocorrência.
2. Compara a palavra encontrada com o termo pesquisado.
3. Se forem iguais, retorna a versão formatada em negrito (`<b>termo</b>`).
4. Caso contrário, retorna a palavra sem modificação.

