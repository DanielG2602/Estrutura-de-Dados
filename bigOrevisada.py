def quicksort(array):
    if len(array) <= 2:
        return array
    else:
        pivot = array[0]
        menores = [x for x in array[1:] if x <= pivot]
        maiores = [x for x in array[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(maiores)
print(quicksort([10, 5, 2, 3]))

def quicksortReverse(array):
    if len(array) <= 2:
        return array
    else:
        pivot = array[0]
        menores = [x for x in array[1:] if x >= pivot]
        maiores = [x for x in array[1:] if x < pivot]
        return quicksortReverse(menores) + [pivot] + quicksortReverse(maiores)
print(quicksortReverse([10, 5, 2, 3]))