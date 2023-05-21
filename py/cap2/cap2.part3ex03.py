"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def valorPagamento(prest, dias):
    """
    Inserir o valor da prestação e os dias de atraso
    """
    valor = (prest * (1 + 0.001) ** dias) + prest * 0.03
    return valor


# PROGRAMA PRINCIPAL
# ENTRADA DE DADOS
prest = float(input("Insira o valor da prestação: "))
dias = int(input("Insira o número de dias de atraso: "))

# PROCESSAMENTO DOS DADOS E SAÍDA
print("Valor a ser pago pelo atraso", valorPagamento(prest, dias))
