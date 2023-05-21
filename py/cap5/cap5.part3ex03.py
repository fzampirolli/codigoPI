"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def mmc(num1, num2):
    a = num1
    b = num2
    resto = None
    while resto is not 0:
        resto = a % b
        a = b
        b = resto
    return (num1 * num2) / a


mmc(12, 15)
