"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

a1 = float(input("Insira um valor inicial: "))
r = float(input("Insira uma razão: "))
for x in range(1, 11):
    num = a1 + (x - 1) * r
    print(num)
