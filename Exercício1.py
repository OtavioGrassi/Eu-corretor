def firstUniqletra(s: str) -> int:

    #Variável para armazenar ocorrencia de caracteres
    Ocorrencias = {}

    #Anda a string inteira e soma a quantidade de vezes que cada caracter aparece
    for letra in s:
        if letra in Ocorrencias: 
             #Se for repetido soma mais 1
            Ocorrencias[letra] += 1
        else:
            #Se for a primeira ocorrencia adiciona 1
            Ocorrencias[letra] = 1
    #Anda pela string novamente e retorna o elemento que tenha aparecido apenas uma vez
    for i in range(len(s)):
        if Ocorrencias[s[i]] == 1:
            return i
    #Senão retorna -1     
    return -1

#Teste
print(firstUniqletra("abacabad"))  
print(firstUniqletra("aaabb"))     