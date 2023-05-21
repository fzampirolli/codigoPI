"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


import math

# DEFINIÇÕES DOS MÉTODOS

def calcAngulo(x, y):
    resposta = math.atan(y / x)
    return resposta

# PROGRAMA PRINCIPAL

print(calcAngulo(2, 0), calcAngulo(2, 2))
