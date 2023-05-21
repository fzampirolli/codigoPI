"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

q = [int(i) for i in input().split(" ") if i]
menor = maior = q[0]
pos_menor = pos_maior = 0

for i in range(len(q)):
    soma += q[i]
    if q[i] < menor:
        menor = q[i]
        pos_menor = i
    if q[i] > maior:
        maior = q[i]
        pos_maior = i

print("Maior valor:", maior)
print("Posição do maior:", pos_maior)
print("Menor valor:", menor)
print("Posição do menor:", pos_menor)
