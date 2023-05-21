"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

# ENTRADA DE DADOS e PROCESSAMENTO
acumulador, contador = 0, 0
print("Entre com 10 notas válidas")
while contador < 10:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("ERRO, nota inválida. Digite uma nota entre 0 e 10:")
        continue
    acumulador += nota
    contador += 1

media = acumulador / contador

# SAÍDA
print("A média das " + str(contador) + " notas é " + str(round(media, 1)))
