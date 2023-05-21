"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def area_trapezio(bMaior, bMenor, h):
    if (bMaior or bMenor) <= 0:
        return print("Insira medidas válidas")
    else:
        A = (h * (bMaior * bMenor)) / 2
        return A


bMaior = float(input("Base maior: "))
bMenor = float(input("Base menor: "))
h = float(input("Altura: "))

print(area_trapezio(bMaior, bMenor, h))
