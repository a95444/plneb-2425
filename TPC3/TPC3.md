
# TPC3 - André Sousa

## Introdução

Este documento explica o processo utilizado para gerar um dicionário de termos médicos a partir de um ficheiro de texto. O foco principal será o tratamento das descrições para garantir uma estrutura organizada e limpa.

## Passos do Processamento

### 1. Leitura do Ficheiro

O primeiro passo foi abrir e ler o conteúdo de um ficheiro '.txt' com as informações a serem apresentadas no dicionário.

```python
with open("dic_med.txt", "r", encoding="utf-8") as file:
    texto = file.read()
```

### 2. Tratamento das Descrições

Através de uma análise inicial do texto capturado pelo método anterior, foi possível identificar incoerências, pois inicialmente havia-se considerado que antes de uma designação existe sempre `\n\n` o que permitiria diferencia-la de uma descrição, contudo no meio de descrições foram também detetados `\n\n`, bem como `\f`.
Logo foi crucial tratar o conteúdo das descrições para permitir uma clara distinção entre os diferentes tipos de conteúdo. Para isso foi utilizada a seguinte expressão regular:

```python
texto = re.sub(r'\n{1,2}\f([a-zA-ZÀ-ÖØ-öø-ÿ|\d]+(.+\n?.+){1,2}\.\n)', r'\g<1>', texto)
```

#### Explicação Detalhada da Expressão Regular:

1. `\n{1,2}` - Captura entre uma e duas quebras de linha que aparecem antes de uma quebra de página.
2. `\f` - Detecta a quebra de página, que indica uma possível separação errada dentro do texto da descrição.
3. `([a-zA-ZÀ-ÖØ-öø-ÿ|\d]+(.+\n?.+){1,2}\.\n)` - Grupo de captura, que guarda o conteúdo de uma descrição: 
   - `[a-zA-ZÀ-ÖØ-öø-ÿ|\d]+` - Deteta o início da descrição capturando a primeira palavra da mesma.
   - `(.+\n?.+){1,2}` - Foi detetado que dentro de algumas descrições existiam quebras de texto, o que influenciava negativamente o resultado pretendido. Logo isto garante que mesmo que existam quebras de texto no meio do texto (no máximo duas), a descrição continuará a ser capturada.
   - `\.\n` - A principal diferença entre uma designação e uma descrição é que a descrição termina com um ponto final seguido de uma quebra de linha. Isto assegura que o que está a ser capturado é efetivamente uma descrição.
4. `\g<1>` - Substitui toda a correspondência apenas pelo grupo capturado, eliminando as quebras de linha e de página indesejadas antes da descrição preservando o conteúdo correto.

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

Após a marcação das designações, os conceitos foram extraídos utilizando expressões regulares que detetam as marcas acrescentadas:

```python
conceitos_raw = re.findall(r"@(.*)\n([^@]*)", texto)
```

Para garantir que as descrições não contêem quebras de linha no seu meio, foi criada a seguinte função para as substituir por apenas 1 espaço:

```python
def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub("\n", " ", descricao)
    return descricao
```

Os conceitos foram então processados para criar uma lista de tuplos que contem a designação e a descrição formatada:

```python
conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]
```

### 6. Gerar a página HTML com o dicionário de termos médicos

Por fim, estes conceitos foram utilizados para gerar uma página HTML que permite representar a informação de forma clara e interpretável.
