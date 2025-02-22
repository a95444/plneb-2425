# TPC2 - André Sousa

## 1.1 hello_start()
**Descrição:** Determina se a palavra "hello" aparece no início da linha.
- **Input:** ["hello world", "goodbye world", "hi, hello there", "hello world, second round"]
- **Output:** ['hello world', 'hello world, second round']

## 1.2 hello_anywhere()
**Descrição:** Determina se a palavra "hello" aparece em qualquer posição da linha.
- **Input:** ["hello world", "goodbye world", "hi, hello there"]
- **Output:** [('hello world', <re.Match object; span=(0, 5), match='hello'>), ('hi, hello there', <re.Match object; span=(4, 9), match='hello'>)]

## 1.3 hello_every()
**Descrição:** Pesquisa por todas as ocorrências da palavra "hello" dentro da linha, admitindo que a palavra seja escrita com maiúsculas ou minúsculas.
- **Input:** "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
- **Output:** ['Hello', 'hello', 'hello', 'HELLO']

## 1.4 hello_yep()
**Descrição:** Pesquisa por todas as ocorrências da palavra "hello" dentro da linha, substituindo cada uma por "*YEP*".
- **Input:** "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
- **Output:** "*YEP* there! Uh, hi, *YEP*, it's me... Heyyy, *YEP*? *YEP*!"

## 1.5 split_function()
**Descrição:** Pesquisa por todas as ocorrências do caracter vírgula, separando cada parte da linha por esse caracter.
- **Input:** "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
- **Output:** ['bananas', 'laranjas', 'maçãs', 'uvas', 'melancias', 'cerejas', 'kiwis', 'etc.']

## 2. palavra_magica()
**Descrição:** Recebe uma frase e determina se a mesma termina com a expressão "por favor", seguida de um sinal válido de pontuação.
- **Input:** ["Posso ir à casa de banho, por favor?", "Preciso de um favor.", "Preciso de um favor, por favor!", "Sai daqui, por favor"]
- **Output:** ('Posso ir à casa de banho, por favor?', True)
('Preciso de um favor.', False)
('Preciso de um favor, por favor!', True)
('Sai daqui, por favor', False)

## 3. narcissismo()
**Descrição:** Calcula quantas vezes a palavra "eu" aparece numa string.
- **Input:** "Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."
- **Output:** "Número total de "eu"s: 6"

## 4. troca_de_curso()
**Descrição:** Substitui todas as ocorrências de "LEI" numa linha pelo nome do curso dado à função.
- **Input:** "LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", "BIOM"
- **Output:** BIOM é o melhor curso! Adoro BIOM! Gostar de BIOM devia ser uma lei.

## 5. soma_string()
**Descrição:** Recebe uma string com vários números separados por uma vírgula (e.g., "1,2,3,4,5") e devolve a soma destes números.
- **Input:** "4,-6,2,3,8,-3,0,2,-5,1"
- **Output:** Resultado da soma: 6

## 6. pronomes()
**Descrição:** Encontra e devolve todos os pronomes pessoais presentes numa frase, i.e., "eu", "tu", "ele", "ela", etc.
- **Input:** "Eu sempre disse que tu e ele viriam, mas Ela e nós preferimos esperar. Vós acham que eles e elas já decidiram?"
- **Output:** Pronomes detetados: ['Eu ', 'tu ', ' ele ', ' Ela ', ' nós', ' Vós', ' eles ', ' elas ']

## 7. variavel_valida()
**Descrição:** Recebe uma string e determina se a mesma é um nome válido para uma variável, ou seja, se começa por uma letra e apenas contém letras, números ou *underscores*.
- **Input:** ["tentativa variavel", "variavel_12345", "var!!123", "123var!!123", "123var123"]
- **Output:** False, True, False, False, False

## 8. inteiros()
**Descrição:** Devolve todos os números inteiros presentes numa string. Um número inteiro pode conter um ou mais dígitos e pode ser positivo ou negativo.
- **Input:** ["teste-12345 0", "-123 45", "novo teste_12345"]
- **Output:** ['-12345', '0'], ['-123', '45'], ['12345']

## 9. underscores()
**Descrição:** Substitui todos os espaços numa string por *underscores*. Se aparecerem vários espaços seguidos, devem ser substituídos por apenas um *underscore*.
- **Input:** ["teste 12345 0", "-123  45 palavra", "novo teste  12345"]
- **Output:** "teste_12345_0", "-123_45_palavra", "novo_teste_12345"

## 10. codigo_postais()
**Descrição:** Recebe uma lista de códigos postais válidos e divide-os com base no hífen. A função deve devolver uma lista de pares.
- **Input:** ["4700-000", "1234-567", "8541-543", "4123-974", "9481-025"]
- **Output:** Lista de pares: [('4700', '000'), ('1234', '567'), ('8541', '543'), ('4123', '974'), ('9481', '025')]

