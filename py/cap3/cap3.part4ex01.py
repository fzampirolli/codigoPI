"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def valida_nota(n1, n2):
    if (n1 or n2) < 0 or (n1 or n2) > 10:
        return print("Insira um valor válido")
    else:
        media = (n1 + n2) / 2
        mediaDeci = "{:.2f}".format(media)
        return mediaDeci


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

print(valida_nota(n1, n2))
