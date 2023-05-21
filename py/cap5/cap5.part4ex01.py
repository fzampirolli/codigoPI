"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

v1 = [int(i) for i in input().split(" ") if i]


def retornaMaisFrequente(v1):
    v2 = [0] * 10
    for i in v1:  # criar o vetor de frequencia
        v2[i] += 1
    print(*v2)
    max = 0
    for i in v2:  # achar o mais frequente
        if max < i:
            max = i
    return max


retornaMaisFrequente(v1)
