"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""


def fatorial(n):
    if n < 0:
        return None  # fatorial de números negativos não existem
    elif n == 0:
        return 1  # fatorial de 0 é 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


print(fatorial(5))  # imprime 120
