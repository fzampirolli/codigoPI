"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def Veri_div(N, D):
    if N % D:
        return True
    else:
        return False


# ENTRADA DE DADOS
N = int(input("Insira dividendo: "))  # Entrada
D = int(input("Insira divisor: "))

# PROCESSAMENTO E SAÍDA
if Veri_div(N, D):
    print("Dividendo não é divisível pelo divisor")
else:
    print("Dividendo é divisível pelo divisor")
