"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def calc(curso, dias):
    if curso == "B":
        return dias * 7 * 15
    elif curso == "I":
        return dias * 8.5 * 20
    elif curso == "A":
        return dias * 10 * 25


# ENTRADA
nome = input("Digite o nome do aluno: ")
dias = int(input("Digite a quantidade de dias na semana: "))
curso = input("Digite o tipo de curso: ")

# PROCESSAMENTO
valor = calc(curso, dias)

# Saída
print("Nome do aluno:", nome)
print("Valor total: R$%d" % (valor))
