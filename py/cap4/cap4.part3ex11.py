"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

e00 = e01 = e02 = " "  # primeira linha do 3x3
e10 = e11 = e12 = " "
e20 = e21 = e22 = " "


def jogar(lin, col, jogador):
    global e00, e01, e02, e10, e11, e12, e20, e21, e22
    if lin == 0 and col == 0:
        e00 = jogador
    if lin == 0 and col == 1:
        e01 = jogador
    if lin == 0 and col == 2:
        e02 = jogador

    if lin == 1 and col == 0:
        e10 = jogador
    if lin == 1 and col == 1:
        e11 = jogador
    if lin == 1 and col == 2:
        e12 = jogador

    if lin == 2 and col == 0:
        e20 = jogador
    if lin == 2 and col == 1:
        e21 = jogador
    if lin == 2 and col == 2:
        e22 = jogador


def verificaColuna(lin):
    return ""


def verificaDiagonal():
    return ""


def verificaLinha(lin):
    global e00, e01, e02, e10, e11, e12, e20, e21, e22
    if lin == 0 and e00 != " " and e00 == e01 and e00 == e02:
        return e00
    if lin == 1 and e10 != " " and e10 == e11 and e10 == e12:
        return e10
    if lin == 2 and e20 != " " and e20 == e21 and e20 == e22:
        return e20
    return ""


def verificaVencedor():
    for i in range(3):
        if verificaLinha(i):
            return "vencedor: " + verificaLinha(i)

        if verificaColuna(i):
            return "vencedor: " + verificaColuna(i)

    if verificaDiagonal():
        return "vencedor: " + verificaColuna(i)

    return ""


def escrever():
    global e00, e01, e02, e10, e11, e12, e20, e21, e22
    s = "{} | {} | {}\n{} | {} | {}\n{} | {} | {}".format(
        e00, e01, e02, e10, e11, e12, e20, e21, e22
    )
    print(s)


cont = 0
while True:
    lin1, col1 = int(input("lin1")), int(input("col1"))  # X
    jogar(lin1, col1, "X")

    r = verificaVencedor()
    if r:
        print(r)
        escrever()
        break

    escrever()
    lin2, col2 = int(input("lin2")), int(input("col2"))  # X
    jogar(lin2, col2, "O")
    escrever()

    r = verificaVencedor()
    if r:
        print(r)
        escrever()
        break
