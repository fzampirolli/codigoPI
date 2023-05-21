"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def valores():
    x = float(input("entre com x: "))
    y = float(input("entre com y: "))
    z = float(input("entre com z: "))
    return x, y, z


def mult(x, y, z):
    m = x * y * z
    return m


# PROGRAMA PRINCIPAL
x, y, z = valores()
print("Produto =", mult(x, y, z))
