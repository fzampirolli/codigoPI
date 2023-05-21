"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DE MÉTODOS:
def delta(a, b, c):
    d = b * b - 4 * a * c
    return d


# PROGRAMA PRINCIPAL
valor = delta(5, -2, 4)
print("O delta de ax^2 + bx + c é %.1f" % valor)
