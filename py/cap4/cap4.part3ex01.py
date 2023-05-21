"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

alturas = []  # Cria uma lista vazia para armazenar as alturas

# Lê 15 alturas e adiciona na lista
for i in range(15):
    altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))
    alturas.append(altura)

# Encontra a menor e a maior altura usando um laço for
menor_altura = alturas[0]
maior_altura = alturas[0]
for altura in alturas:
    if altura < menor_altura:
        menor_altura = altura
    if altura > maior_altura:
        maior_altura = altura

# Mostra os resultados
print("A menor altura do grupo é:", menor_altura)
print("A maior altura do grupo é:", maior_altura)