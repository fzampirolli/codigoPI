"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def lerNotas():
    return float(input("P1: ")), float(input("P2: ")), float(input("Proj.: "))


def calcMediaPond():
    return p1 * 0.3 + p2 * 0.4 + proj * 0.3


def escreveNotas(nome):
    ss = f"Aluno: {nome}\nProva1: {p1:.2f}\nProva1: {p2:.2f}\nProjeto: {proj:.2f}\nMédia: {m:.2f}"
    print(ss)


# PROGRAMA PRINCIPAL
# ENTRADA DE DADOS
p1, p2, proj = lerNotas()

# PROCESSAMENTO DOS DADOS
m = calcMediaPond()

# SAÍDA
escreveNotas("Ana Maria Chavier")
