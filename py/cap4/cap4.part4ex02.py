"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

x = int(input("Insira um valor de base: "))
y = int(input("Insira um valor de expoente: "))
pot = 1
for i in range(1, y + 1):
    pot = pot * x

print(pot)
