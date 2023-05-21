"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

import math  # Importa o módulo math para usar a função factorial()

# Lê valores de m até que o usuário digite um valor negativo
while True:
    m = int(input("Digite um valor para m (negativo para encerrar): "))
    if m < 0:
        break  # Sai do loop se um valor negativo for lido

    # Verifica se m é par
    if m % 2 == 0:
        divisores = 0
        for i in range(1, m + 1):
            if m % i == 0:
                divisores += 1
        print("O número {} é par e possui {} divisores.".format(m, divisores))

    # Verifica se m é ímpar e menor do que 10
    elif m % 2 == 1 and m < 10:
        fatorial = math.factorial(m)
        print(
            "O número {} é ímpar e menor do que 10. Seu fatorial é {}.".format(
                m, fatorial
            )
        )

    # Verifica se m é ímpar e maior ou igual a 10
    elif m % 2 == 1 and m >= 10:
        soma = 0
        for i in range(1, m + 1):
            soma += i
        print(
            "O número {} é ímpar e maior ou igual a 10. A soma dos inteiros de 1 até {} é {}.".format(
                m, m, soma
            )
        )
