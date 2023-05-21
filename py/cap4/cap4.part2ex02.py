"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    ant1 = 1  # 1º número anterior
    ant2 = 0  # 2º número anterior
    soma = 0
    for contador in range(1, n):
        soma = ant1 + ant2  # soma dos 2 números anteriores
        ant1, ant2 = soma, ant1
    return soma


n = int(input("Insira n: "))

print("F(%d) = %d" % (n, fibonacci(n)))
