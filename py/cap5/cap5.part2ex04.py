"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import numpy as np


def trocaValores(vetor, i, j):
    if (0 <= i < len(vetor)) and (0 <= j < len(vetor)):
        t = vetor[i]
        vetor[i] = vetor[j]
        vetor[j] = t
    return vetor


n = int(input("Número de elementos do vetor: "))
v = np.zeros(n).astype(int)

print("Digite " + str(n) + " Valores: ")
for i in range(n):
    v[i] = int(input())

i = int(input("Posição i que você deseja trocar: "))
j = int(input("Posição j que você deseja trocar: "))

print("Vetor original:", *v)
print("Vetor trocado: ", *trocaValores(v, i, j))
