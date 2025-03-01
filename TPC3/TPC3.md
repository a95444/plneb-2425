
# Geração de um Dicionário de Termos Médicos a partir de um Ficheiro TXT

## Introdução

Este documento explica o processo utilizado para gerar um dicionário de termos médicos a partir de um ficheiro de texto. O foco principal será o tratamento das descrições para garantir uma estrutura organizada e limpa.

## Passos do Processamento

### 1. Leitura do Ficheiro

O primeiro passo foi abrir e ler o conteúdo do ficheiro `dic_med.txt`.

```python
with open("dic_med.txt", "r", encoding="utf-8") as file:
    texto = file.read()
```

### 2. Tratamento das Descrições

O texto original apresentava algumas inconsistências, como quebras de linha e quebras de página (`\f`) antes de algumas descrições. Para limpar isso, foi utilizada a seguinte expressão regular:

```python
texto = re.sub(r'\n{1,2}\f([a-zA-ZÀ-ÖØ-öø-ÿ|\d]+(.+\n?.+){1,2}\.\n)', r'\g<1>', texto)
```

#### Explicação Detalhada da Expressão Regular:

1. `\n{1,2}` - Captura entre uma e duas quebras de linha que aparecem antes de uma quebra de página.
2. `\f` - Detecta a quebra de página, que indica uma possível separação errada dentro do texto.
3. `([a-zA-ZÀ-ÖØ-öø-ÿ|\d]+(.+\n?.+){1,2}\.\n)`:
   - `[a-zA-ZÀ-ÖØ-öø-ÿ|\d]+` - Captura a primeira palavra da descrição, que pode ser um termo médico composto por letras ou números.
   - `(.+\n?.+){1,2}` - Garante que a descrição tenha pelo menos uma frase completa, permitindo até duas linhas para capturar textos que se estendem por múltiplas linhas.
   - `\.\n` - Garante que o trecho capturado termina com um ponto final seguido de uma quebra de linha, assegurando que a descrição esteja completa.
4. `\g<1>` - Substitui toda a correspondência apenas pelo grupo capturado, eliminando as quebras de linha extras antes da descrição e preservando o conteúdo correto.

Este passo permitiu:

- Remover as quebras de página e quebras de linha que dividiam de forma inadequada as descrições.
- Preservar a estrutura original do texto sem perder informações importantes.
- Garantir que cada descrição se mantenha coesa e completa dentro do dicionário.

### 3. Remoção de Quebras de Página

Após o tratamento das descrições, foi necessário remover todas as quebras de página restantes:

```python
texto = re.sub(r"\f", "", texto, 0)
```

### 4. Marcação das Designações

Para separar os termos médicos das suas descrições, as designações foram marcadas com `@`:

```python
texto = re.sub(r"\n\n", "\n\n@", texto, 0)
```

### 5. Extração e Limpeza das Descrições

Após a marcação das designações, os conceitos foram extraídos utilizando expressões regulares:

```python
conceitos_raw = re.findall(r"@(.*)\n([^@]*)", texto)
```

Para garantir que as descrições estivessem limpas, foi criada a função:

```python
def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub("\n", " ", descricao)
    return descricao
```

Os conceitos foram então processados para criar uma lista de tuplos contendo a designação e a descrição formatada:

```python
conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]
```

