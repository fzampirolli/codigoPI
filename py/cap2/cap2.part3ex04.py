"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

# DEFINIÇÕES DOS MÉTODOS
import math


def combinacao(p, n):
    r = math.factorial(n) / (math.factorial(p) * (math.factorial(n - p)))
    return r


# PROGRAMA PRINCIPAL
# ENTRADA DE DADOS
n = 6
p = 5
# PROCESSAMENTO DOS DADOS
r = combinacao(p, n)
# SAÍDA
print(r)
