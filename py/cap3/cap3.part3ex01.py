"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

capacidadeMax = float(input("Qual a capacidade máxima do elevador?"))
p1 = float(input("Digite o peso da primeira pessoa: "))
p2 = float(input("Digite o peso da segunda pessoa: "))
p3 = float(input("Digite o peso da terceira pessoa: "))
p4 = float(input("Digite o peso da quarta pessoa: "))
p5 = float(input("Digite o peso da quinta pessoa: "))

pesoTotal = p1 + p2 + p3 + p4 + p5

if pesoTotal > capacidadeMax:
    print("O elevador excedeu a carga máxima!")
else:
    print("O elevador está liberado para subir.")
