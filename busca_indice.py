# O algoritmo busca o índice de um valor em uma matriz, dado um alvo X

matriz= [5, 6, 7, 9, 10, 11, 14, 17, 19, 20, 21, 30]
item = 6

def busca(matriz, item):
    indice = 0
    for i in range(len(matriz)):
        if matriz[i] == item:
            indice = i
            break
    return indice

print(busca(matriz, item))    