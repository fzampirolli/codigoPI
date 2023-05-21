"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def imc(peso, alt):
    imc = peso / (alt**2)
    if imc > 35:
        return "Morbidez"
    if imc > 30:
        return "Obeso"
    if imc > 25:
        return "Acima do Peso"
    if imc > 18.5:
        return "Saudável"
    else:
        return "Magro"


# ENTRADA DE DADOS
peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

# PROCESSAMENTO E SAÍDA
print("Sua classificação:", imc(peso, altura))
