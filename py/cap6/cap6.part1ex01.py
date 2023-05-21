"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import numpy as np  # muito útil para trabalhar com vetor!


def leiaMatriz(L, C):
    m = np.zeros((L, C)).astype(int)  # matriz de inteiro com Linhas x Colunas
    for i in range(L):
        for j in range(C):
            m[i][j] = int(input())
    return m


def escrevaMatriz(m):
    s = ""  # existem várias forma de formatar uma matriz
    for i in range(len(m)):
        for j in range(len(m[0])):
            s += str(m[i][j]) + "\t"
        s += "\n"
    print(s)


def escrevaMatriz_v2(m):
    for i in range(len(m)):
        print(*m[i])


# ENTRADA DE DADOS
L = int(input("Digite o numero de alunos:"))
C = int(input("Digite o numero de avaliações:"))
C = C + 1  # a primeira coluna é o RA do aluno
m = leiaMatriz(L, C)
# L,C = np.random.randint(2,10, size = 2) # INTERESSANTE para testar
# print(L,C)
# m = np.random.randint(10, size=(L,C))   # INTERESSANTE para testar

# PROCESSAMENTO ?
# SAÍDA DE DADOS
print("LISTA DE ALUNOS vs Avaliações:")
s = "RA"
for i in range(C - 1):
    s += "\t" + str(i + 1)
print(s)
escrevaMatriz(m)
