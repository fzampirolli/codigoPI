"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

a1 = float(input("Valor inicial: "))
q = float(input("Razão: "))
for n in range(1, 11):
    print(a1 * (q ** (n - 1)))
