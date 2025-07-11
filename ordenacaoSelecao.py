def buscarMenor(arr):
    low = arr[0]
    low_index = 0
    for i in range(1, len(arr)):
        if arr[i] < low:
            low = arr[i]
            low_index = i
    return low_index
    
def ordenacao_selecao(arr):
    newArr = []
    for i in range(len(arr)):
        low = buscarMenor(arr)
        newArr.append(arr[low])
        arr.pop(low)
        
    return newArr


print(ordenacao_selecao([5,3,6,2,10]))