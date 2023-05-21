"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

# Inicializa as variáveis de contagem e soma
quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_geral = 0

# Lê números até que o usuário digite zero
while True:
    numero = int(input("Digite um número (zero para encerrar): "))
    if numero == 0:
        break  # Sai do loop se o número zero for lido

    # Verifica se o número é par ou ímpar e atualiza as variáveis de contagem e soma
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
    soma_geral += numero

# Calculaas médias
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0
if quantidade_pares + quantidade_impares > 0:
    media_geral = soma_geral / (quantidade_pares + quantidade_impares)
else:
    media_geral = 0

# Escreve os resultados na tela
print("Quantidade de números pares: {}".format(quantidade_pares))
print("Quantidade de números ímpares: {}".format(quantidade_impares))
print("Média de valores pares: {:.2f}".format(media_pares))
print("Média geral dos números lidos: {:.2f}".format(media_geral))
