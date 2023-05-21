"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

qttd = soma = 0

n = int(input())  # primeira entrada para acionar o laço
while n >= 0:
    qttd += 1
    soma += n
    n = int(input())  # se for <0 já encerra laço

print("Quantidade de números:", qttd)
print("Somatório dos valores:", soma)
if qttd:
    print("Média aritmética:", soma / qttd)
