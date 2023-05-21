"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import numpy as np  # muito útil para trabalhar com vetor!


# MÉTODOS
def leiaVetor(n):
    v = np.zeros(n).astype(int)  # aloca vetor de inteiro com n elementos
    for i in range(n):
        v[i] = int(input())
    return v


def escrevaVetor(v):
    for i in range(n):
        print(v[i])


# ENTRADA DE DADOS
n = int(input("Digite o tamanho do vetor:"))
print("Entre com " + str(n) + " elementos:")
v1 = leiaVetor(n)

v2 = np.zeros(n).astype(int)

# PROCESSAMENTO
for i in range(n):
    max = v1[i]
    if i - 1 >= 0 and max < v1[i - 1]:
        max = v1[i - 1]
    if i + 1 < n and max < v1[i + 1]:
        max = v1[i + 1]
    v2[i] = max

# SAÍDA DE DADOS
print("v2:")
escrevaVetor(v2)
