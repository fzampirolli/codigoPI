"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS


def valores(A, B, C, D):
    if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
        return "valores aceitos"
    else:
        return "valores não aceitos"


A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
D = float(input("D: "))

print(valores(A, B, C, D))
