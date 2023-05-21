"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS


def verificaBissexto():
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        print("O ano é bissexto")
    else:
        print("O ano não é bissexto")


ano = int(input("Digite seu ano: "))

verificaBissexto()
