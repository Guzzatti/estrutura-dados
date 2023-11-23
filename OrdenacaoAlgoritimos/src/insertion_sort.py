from geraVetor import geraVetor

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Exemplo de uso:
vetor_2 = geraVetor(10000)
insertion_sort(vetor_2)