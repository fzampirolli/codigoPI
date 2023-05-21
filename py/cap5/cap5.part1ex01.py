"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import numpy as np  # muito útil para trabalhar com vetor!

# ENTRADA DE DADOS
n = int(input("Digite o numero de alunos:"))
ra = np.zeros(n).astype(int)  # vetor de inteiros com n elementos
nome = np.zeros(n).astype(str)  # vetor de strings com n elementos
for i in range(n):
    ra[i] = int(input("RA:"))
    nome[i] = input("Nome:")
# PROCESSAMENTO ?
# SAÍDA DE DADOS
print("LISTA DE ALUNOS\nNúmero\t RA\t Nome")
for i in range(n):
    print(i + 1, "\t", ra[i], "\t", nome[i])
