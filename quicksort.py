def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice                         

def ordenacaoporSelecao(arr):
    novoArr = []
    while len(arr) > 0: 
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr  

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))
