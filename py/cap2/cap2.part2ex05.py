"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

base, altura, area = 2, 3, 6


# DEFINIÇÕES DOS MÉTODOS
def calcBase():
    return area / altura


def calcAltura():
    return area / base


def calcArea():
    return base * altura


# PROGRAMA PRINCIPAL

print(calcBase(), calcAltura(), calcArea())
