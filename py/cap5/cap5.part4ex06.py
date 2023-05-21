"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

v = [int(i) for i in input().split(" ") if i]
contador = soma = 0

for i in range(len(v)):
    soma += v[i]

media = soma / len(v)
for i in v:
    if i > media:
        contador += 1

print("Média:", media)
print("Quantos acima da media:", contador)
