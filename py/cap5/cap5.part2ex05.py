"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def geraVetor(v1):
    vetor = [int(i) for i in v1.split(" ") if i]

    return vetor


def mudaPosicao(vetor):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[i] > vetor[j]:
                print("i=", i, "j=", j)
                print(*vetor)
                T = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = T
                print(*vetor)

    return vetor


v1 = input()
vetor = geraVetor(v1)
vetor = mudaPosicao(vetor)
print(vetor)
