def mesclar_intervals(intervalos):
    # Organiza os intervalos utilizando elemento 0 de cada tupla
    intervalos.sort(key=lambda x: x[0])
    
    # Lista para guardar os intervalos agrupados
    resultado = []
    
    for intervalo in intervalos:
        # Se o resultado for vazio ou não se sobrepõe do último, adiciona ele mesmo
        if not resultado or resultado[-1][1] < intervalo[0]:
            resultado.append(intervalo)
        else:
            # Casocontrário sobrepõe os intervalos
            resultado[-1][1] = max(resultado[-1][1], intervalo[1])
    
    return resultado

#Testes
print(mesclar_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))

print(mesclar_intervals([[1, 4], [4, 5]]))