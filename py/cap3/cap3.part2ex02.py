"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def Ordena(A, B, C):
    if A > B and A > C:
        if B > C:
            return A, B, C
        else:
            return A, C, B
    elif B > A and B > C:
        if A > C:
            return B, A, C
        else:
            return B, C, A
    else:
        if A > B:
            return C, A, B
        else:
            return C, B, A


# ENTRADA DE DADOS
A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))

# Processamento
A, B, C = Ordena(A, B, C)

# Saída
print(C, "<", B, "<", A)
