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

## 7. s_balanced()
**Descrição:** Verifica se todos os caracteres de uma string estão presentes em outra.
- **Input:** "banana", "banana OrangoTAngo"
- **Output:** True

## 8. count_ocorrences()
**Descrição:** Conta quantas vezes uma string aparece dentro de outra.
- **Input:** "bAnana", "bananabanaNabananaBananabanana"
- **Output:** 5

## 9. check_anagrama()
**Descrição:** Verifica se duas strings são anagramas.
- **Input:** "saudade", "aduesad"
- **Output:** True

## 10. anagram_classes()
**Descrição:** Agrupa palavras que são anagramas na mesma classe.
- **Input:** ["saudade", "aduesad", "sacar", "casar", "listen", "silent"]
- **Output:** {'aaddesu': ['saudade', 'aduesad'], 'aacrs': ['sacar', 'casar'], 'eilnst': ['listen', 'silent']}

