# TPC10 - PG52564

## 1. Pré-processamento

1. **Leitura do texto**  
   Carregámos o livro completo e dividimo-lo em frases usando `sent_tokenize`.

2. **Tokenização**  
   Cada frase foi transformada numa lista de tokens (`word_tokenize`), convertida para minúsculas e filtrada para manter apenas tokens alfabéticos.

3. **Estrutura de treino**  
   O resultado foi uma lista de listas, onde cada sub-lista corresponde a uma frase tokenizada, pronta para alimentar o Word2Vec.

## 2. Treino do Modelo Word2Vec

- **Parâmetros principais**  
  - `vector_size=500` (dimensão dos vetores)  
  - `window=5` (tamanho da janela de contexto)  
  - `min_count=10` (ignorar termos com frequência inferior)  
  - `workers=os.cpu_count()` (uso de todos os núcleos disponíveis)

- **Objetivo**  
  Capturar relações semânticas e sintáticas entre as palavras do livro, de modo a podermos depois medir similaridades e resolver analogias.

- **Armazenamento**  
  Salvámos o modelo treinado em disco para cargas e testes futuros, sem ter de re-treinar a cada execução.

## 3. Testes Realizados

### 3.1 `most_similar('harry')`

**O quê?**  
Lista de palavras cujos vetores estão mais próximos de “harry”.

**Porquê?**  
Verificar se o modelo agrupa corretamente personagens e termos do universo bruxo (ex: “hermione”, “ron”, “hogwarts”).

---

### 3.2 Similaridades Pontuais

| Par                   | Motivação                                        | Exemplo de saída |
|-----------------------|--------------------------------------------------|------------------|
| `("harry","draco")`   | Protagonista × antagonista principal             | ~0.62            |
| `("harry","malfoy")`  | Variação de sobrenome, mesmo personagem          | ~0.81            |
| `("harry","trouxa")`  | Bruxo × não-bruxo (muggle)                       | ~0.12            |
| `("hermione","trouxa")`| Personagem principal feminina × não-bruxo        | ~0.08            |
| `("harry","voldemort")`| Herói × vilão central                            | ~0.35            |
| `("hermione","voldemort")`| Protagonista feminina × vilão                 | ~0.29            |

> **Porquê?**  
> Esses pares testam se a co-ocorrência e o contexto no texto refletem relações narrativas: proximidade alta entre personagens que aparecem juntos, e baixa entre bruxos e “trouxas”.

---

### 3.3 Testes de Analogia

```python
# Exemplo: “harry” – “trouxa” + “bruxo” ≈ ?
model.wv.most_similar(positive=['harry','bruxo'], negative=['trouxa'])
```

- **Objetivo:** Verificar se o modelo aprendeu a diferença _bruxo × trouxa_ no mesmo espaço que _harry_ (e.g. “harry”/“trouxa” → “harry”/“bruxo” dá “hermione” ou outra figura mágica).
- **Comentário:** Normalmente retorna um nome de outro bruxo ou termo mágico, confirmando o mapa semântico.

Outro exemplo:
```python
analogy('bruxo', 'menina', 'menino')
```
- **Objetivo:** Encontrar o equivalente a “menina” no universo dos bruxos, partindo da relação  bruxo_ - menino_.

---

### 3.4 Visualização com t-SNE

- Selecionámos um conjunto de palavras-chave (e.g. `["harry","hermione","voldemort","trouxa","bruxo","muggle"]`) e projetámo-las em 2D usando t-SNE.
- **Objetivo:** Inspecionar visualmente se termos mágicos se agrupam separadamente de “trouxa”/“muggle” e observar clusterização de personagens.

- - Selecionámos um novo conjunto de palavras-chave `['harry', 'rony', 'hermione', 'hagrid', 'neville', 'potter', 'granger', 'weasley', 'percy', 'malfoy', 'draco', 'dumbledore','varinha', 'pedra','madeira', 'porta','medo', 'triste', 'feliz', 'alegremente']` e projetámo-las em 2D usando t-SNE.
- **Objetivo:** Inspecionar visualmente se pessoas, objetos e sentimenos se agrupam separadamente.

---

### 3.5 Treino Incremental

- Demonstrámos como **continuar a treinar** o modelo com novo texto:
  ```python
  model.build_vocab(more_sentences, update=True)
  model.train(more_sentences, total_examples=model.corpus_count, epochs=model.epochs)
  ```
- **Porquê?**  
  Permite enriquecer o vocabulário e ajustar os vetores sem re-treinar do zero.

---

## 4. Resultados e Observações

- **Relações bem capturadas:**  
  Proximidade alta entre “harry” e “ron”/“hermione”; baixa entre “harry” e “trouxa”.  
- **Analogias razoáveis:**  
  Expressões como _“harry” – “trouxa” + “bruxo”_ devolvem nomes de bruxos conhecidos.
- **Limitações notadas:**  
  - Termos raros (frequência < min_count) são ignorados.  
  - Vetor de dimensão alta (500) num corpus de um só livro pode levar a sobreajuste.  
  - Analogia complexa (e.g. relacionamentos sociais) nem sempre reflete a narrativa inteira.

---

## 5. Análise Crítica

1. **Cobertura de Vocabulário**  
   Embora min_count=10 garanta qualidade estatística, perde-se termos importantes que aparecem poucas vezes, como nomes secundários.

2. **Parametrização**  
   - `vector_size=500` mostrou-se exagerado para um único livro, aumentando custo computacional sem grande ganho de qualidade.  
   - Window size 5 foi adequado para capturar co-ocorrência local, mas explorar janelas maiores (10–15) podia ajudar em relações de personagem.

3. **Qualidade das Analogias**  
   - Modelos Word2Vec em textos narrativos tendem a refletir relações de contexto (personagens que falam juntos), mas podem falhar em analogias abstratas fora do vocabulário central.

4. **Incremental Training**  
   Útil para experimentar novo texto (por ex., continuação dos livros), mas é crucial normalizar e limpar bem o material adicional.
