"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def mmc(n1, n2):
    i = 2
    mmc = 1
    while n1 != 1 or n2 != 1:
        if n1 % i == 0 and n2 % i == 0:
            n1 /= i
            n2 /= i
            mmc *= i
        elif n1 % i == 0:
            n1 /= i
            mmc *= i
        elif n2 % i == 0:
            n2 /= i
            mmc *= i
        else:
            i += 1
    return mmc


n1 = int(input("Insira o 1º número: "))
n2 = int(input("Insira o 2º número: "))

print("MMC:", mmc(n1, n2))
