"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import numpy as np  # muito útil para trabalhar com vetor!


# MÉTODO(S)
def leiaVetor(n):
    v = np.zeros(n).astype(int)  # aloca vetor de inteiro com n elementos
    for i in range(n):
        v[i] = int(input())
    return v


# ENTRADA DE DADOS
n = int(input("Digite o numero de alunos:"))
print("Entre com " + str(n) + " RAs:")
ras = leiaVetor(n)
print("Entre com " + str(n) + " Notas:")
notas = leiaVetor(n)

# PROCESSAMENTO
# ?

# SAÍDA DE DADOS
print("LISTA DE ALUNOS")
print("Número\t RA\t Nota")
for i in range(n):
    print(i + 1, "\t", ras[i], "\t", notas[i])
