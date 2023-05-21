"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

C_str = input()
C = int(C_str)
F = C * 9 / 5 + 32
print(f"{C} graus Celsius corresponde a {F:.1f} graus Fahrenheit")  # mais intuitivo
print("%d graus Celsius corresponde a %.1f graus Fahrenheit" % (C, F))  # ou
print(C, "graus Celsius corresponde a", F, "graus Fahrenheit")  # ou, ruim para formatar
