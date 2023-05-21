"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

v = [int(i) for i in input().split(" ") if i]
pares = []
menor = maior = v[0]
soma = contador = 0

for i in range(len(v)):
    soma += v[i]
    if v[i] % 2 == 0:
        pares.append(v[i])
    if v[i] < menor:
        menor = v[i]
    if v[i] > maior:
        maior = v[i]

media = soma / len(v)
for i in v:
    if i > media:
        contador += 1

print("Lista dos pares:", *pares)
print("Menor valor:", menor)
print("Maior valor:", maior)
print("Média:", media)
print("Quantos acima da media:", contador)
