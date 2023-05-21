"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def encontraMenor(A, B, C):
    T = 0
    if A > B:
        T = A
        A = B
        B = T
    if A > C:
        T = A
        A = C
        C = T
    if B > C:
        T = B
        B = C
        C = T

    return A, B, C

# ENTRADA DE DADOS
A, B, C = int(input()), int(input()), int(input())

# PROCESSAMENTO E SAÍDA
print(encontraMenor(A, B, C))
