"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

# Inicializa as variáveis de contagem
contagem_0_25 = 0
contagem_26_50 = 0
contagem_51_75 = 0
contagem_76_100 = 0

# Lê números até que um número negativo seja digitado
while True:
    numero = int(input("Digite um número (negativo para encerrar): "))
    if numero < 0:
        break  # Sai do loop se um número negativo for lido

    # Incrementa a contagem correspondente ao intervalo em que o número se encontra
    if numero >= 0 and numero <= 25:
        contagem_0_25 += 1
    elif numero >= 26 and numero <= 50:
        contagem_26_50 += 1
    elif numero >= 51 and numero <= 75:
        contagem_51_75 += 1
    elif numero >=76 and numero <= 100:
       contagem_76_100 += 1

# Mostra os resultados
print("Quantidade de números no intervalo [0-25]:", contagem_0_25)
print("Quantidade de números no intervalo [26-50]:", contagem_26_50)
print("Quantidade de números no intervalo [51-75]:", contagem_51_75)
print("Quantidade de números no intervalo [76-100]:", contagem_76_100)