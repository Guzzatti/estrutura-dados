from geraVetor import geraVetor

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Exemplo de uso:
vetor_4 = geraVetor(10000)
vetor_4 = quick_sort(vetor_4)