"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


import numpy as np


def leiaVetor(n):
    v = np.zeros(n).astype(int)
    for i in range(n):
        v[i] = int(input())
    # v = [int(i) for i in input().split(' ') if i] # ou de forma compactar
    return v


n = int(input("Digite o número de alunos: "))
print("Entre com " + str(n) + " Notas: ")
nota = leiaVetor(n)
notaMax, notaMin = nota[0], nota[0]

for i in range(1, n):
    if notaMax < nota[i]:
        notaMax = nota[i]
    if notaMin > nota[i]:
        notaMin = nota[i]
print("Maior nota:", notaMax, "\nMenor nota:", notaMin)
