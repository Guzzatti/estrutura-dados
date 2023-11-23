import random

def geraVetor(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

# Exemplo de uso:
vetor = geraVetor(10000)