"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

numero = int(input("digite o numero: "))
unidade = numero % 10
numero = (numero - unidade) / 10
dezena = numero % 10
numero = (numero - dezena) / 10
centena = numero
dezena = int(dezena)
centena = int(centena)
# print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')
print(unidade + dezena + centena)
