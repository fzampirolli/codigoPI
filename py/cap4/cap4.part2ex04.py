"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

I = float(input("Insira o investimento inicial: "))
n = int(input("Insira o número de meses: "))
Jn = float(input("Insira a taxa de juros ao mês em porcentagem: "))

for x in range(n + 1):
    M = I * ((1 + Jn / 100) ** x)
    Jt = M - I
    print("%5d %20.2f %20.2f %20.2f" % (x, Jn, Jt, M))
