"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import math

# DEFINIÇÕES DOS MÉTODOS

def calcAngulo(x1, y1, x2, y2):
    resposta = math.atan((y2 - y1) / (x2 - x1))
    return resposta

# PROGRAMA PRINCIPAL

print(calcAngulo(0, 0, 2, 0), calcAngulo(0, 1, 2, 2))
