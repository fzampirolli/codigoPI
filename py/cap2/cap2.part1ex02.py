"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DE MÉTODOS:
def leia():
    a = float(input("Entre com o valor de a:"))
    b = float(input("Entre com o valor de b:"))
    c = float(input("Entre com o valor de c:"))
    return a, b, c


def escreva(d):
    print("Delta =", d)


def delta(a, b, c):
    d = b * b - 4 * a * c
    return d


# PROGRAMA PRINCIPAL

# ENTRADA DE DADOS
a, b, c = leia()

# PROCESSAMENTO
d = delta(a, b, c)

# SAÍDA DE DADOS4
escreva(d)
