from collections import deque

def ladderLength(inicio, fim, dicionario):
    if fim not in dicionario:
        return 0, [] #Se a palavra final não estiver no dicionário não será possivel resolver
    
    fila = deque([(inicio, [inicio])])  # Inicia com a palavra inicial e a quantidade de transformações
    visitados = set([inicio])  # Armazena palavras já visitadas

    while fila:
        palavra_atual, caminho = fila.popleft() #Remove o primeiro item à esquerda

        if palavra_atual == fim:
            return len (caminho), caminho

        for i in range(len(palavra_atual)):
            for letra in 'abcdefghijklmnopqrstuvwxyz':  # Tenta trocar cada letra
                nova_palavra = palavra_atual[:i] + letra + palavra_atual[i+1:]
                if nova_palavra in dicionario and nova_palavra not in visitados:
                    fila.append((nova_palavra, caminho + [nova_palavra]))
                    visitados.add(nova_palavra)

    return 0, []  # Se não encontrar uma resposta, retorna 0


passos, sequencia = ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(f"{passos}", f"{sequencia}")

passos, sequencia = ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
print(f"{passos}", f"{sequencia}")