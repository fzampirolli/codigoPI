"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

medsal = medson = percent = popu = popusal = popuson = qtdsal = maiorsal = 0

while True:
    sal = float(input())
    if sal >= 0:
        filhos = int(input())
        popu += 1
        popusal += sal
        popuson += filhos
        if sal <= 10000:
            qtdsal += 1
        if sal > maiorsal:
            maiorsal = sal
    else:
        break

if popu > 0:
    medsal = popusal / popu
    medson = popuson / popu
    percent = (qtdsal / popu) * 100

print(f"{medsal:.2f} {medson:.2f} {percent:.2f} {maiorsal:.2f}")
