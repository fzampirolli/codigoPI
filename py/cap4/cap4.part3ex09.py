"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def myMaior(a, b):
    if a > b:
        return a
    else:
        return b


condicao = True
c1 = c2 = c3 = c4 = n = b = 0
while condicao:
    voto = int(input("Qual o seu voto? "))
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        c4 += 1
    elif voto == 5:  # nulo
        n += 1
    elif voto == 6:  # branco
        b += 1
    elif voto == 0:
        condicao = False
print("Total de votos para cada candidato 1:", c1)
print("Total de votos para cada candidato 2:", c2)
print("Total de votos para cada candidato 3:", c3)
print("Total de votos para cada candidato 4:", c4)
print("Total de votos nulos:", n)
print("Total de votos brancos:", b)
print("Maior número de votos:", myMaior(c4, myMaior(c3, myMaior(c1, c2))))
