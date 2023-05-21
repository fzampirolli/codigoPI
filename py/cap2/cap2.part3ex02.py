"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def somaImposto(taxa, custo):
    valor = custo * (1 + (taxa / 100))
    return valor


# PROGRAMA PRINCIPAL

# ENTRADA DE DADOS
taxa = float(input("Insira a quantia de imposto em porcentagem: "))
custo = float(input("Insira o custo do produto: "))

# PROCESSAMENTO E SAÍDA
print("O custo do produto com o imposto é de R$ %.2f" % somaImposto(taxa, custo))
