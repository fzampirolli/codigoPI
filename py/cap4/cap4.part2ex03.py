"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

cont = 0


def primo(n):
    cont = 0
    for x in range(1, n):
        if n % x == 0:
            cont += 1
        if cont >= 2:
            return 0
    return 1


n = int(input())

if primo(n):
    print("É primo")
else:
    print("Não é primo")
