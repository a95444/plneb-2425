#TPC1 - ANDRE SOUSA

#1. given a string “s”, reverse it.
def reverse_string(s):
    return s[::-1]
print(f'Exercício 1: {reverse_string("teAtro cIrCo")}')


# 2. given a string “s”, returns how many “a” and “A” characters are present in it.
def get_a_A(s):
    nr_a= s.count("a")
    nr_A= s.count("A")
    return (nr_a, nr_A)
print(f'Exercício 2: a:{get_a_A("bananA OrangoTAngo")[0]}, A:{get_a_A("bananA OrangoTAngo")[1]} ')


 #3. given a string “s”, returns the number of vowels there are present in it.
def get_vowels(s):
    vowels="aeiou"
    s=s.lower()
    contador=0
    for letter in s:
        if letter in vowels:
            contador+=1
    return contador
print(f'Exercício 3: Número de vogais: {get_vowels("bananA OrangoTAngo")}')

 #4. given a string “s”, convert it into lowercase.
def s_lowercase(s):
     return s.lower()
x="AbCdEf GhIj"
print(f'Exercício 4: original: {x}, alterado: {s_lowercase(x)}')

 #5. given a string “s”,  convert it into uppercase.
def s_uppercase(s):
     return s.upper()
print(f'Exercício 5: original: {x}, alterado: {s_uppercase(x)}')

 #6. Verifica se uma string é capicua
def check_capicua(s):
     if s_lowercase(reverse_string(s))==s_lowercase(s):
         return True
     else:
         return False
y="aVA"
print(f'Exercício 6: original: {y}, é capicua: {check_capicua(y)}')


#7. Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão
#balanceadas se todos os caracteres de s1 estão presentes em s2.)
def s_balanced(s1,s2):
    for letter in s1:
        if letter not in s2:
            return False
    return True

x1="banana"
x2="banana OrangoTAngo"
print(f'Exercício 7: As strings s1: {x1} e s2: {x2} estão balanceadas? R:{s_balanced(x1,x2)}')

#8. Calcula o número de ocorrências de s1 em s2
def count_ocorrences(s1,s2):
     return (s2.lower()).count(s1.lower())
y1="bAnana"
y2="bananabanaNabananaBananabanana"
print(f'Exercício 8: Número de ocorrências de "{y1}" em "{y2}": {count_ocorrences(y1, y2)}')

#9. Verifica se s1 é anagrama de s2.
#○ "listen" e "silent": Deve imprimir True
#○ "hello", "world": Deve imprimir False
def check_anagrama(s1,s2):
    if sorted(s1.lower())==sorted(s2.lower()):
        return True
    else:
        return False
z1="saudade"
z2="aduesad"
print(f'Exercício 9: check_anagrama de {z1} e {z2}: {check_anagrama(z1,z2)}')


# 10. Dado um dicionário, calcular a tabela das classes de anagramas.

def anagram_classes(lista_s):
    classes={}
    for s in lista_s:
        #print(s)
        letras = sorted(s) # o sorted cria uma lista.
        palavra="".join(letras)

        if palavra not in classes:
            classes[palavra]=[]
            classes[palavra].append(s)
        else:
            classes[palavra].append(s)
    return classes

lista = ["saudade", "aduesad", "sacar", "casar", "listen", "silent"]
print(f'Exercício 10: classes anagramas: {anagram_classes(lista)}')
