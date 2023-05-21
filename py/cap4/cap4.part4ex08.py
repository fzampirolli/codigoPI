"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

# Lê pares de valores m e n até que o usuário digite um par com valor n igual a 0
while True:
    m = int(input("Digite o valor de m: "))
    n = int(input("Digite o valor de n: "))
    if n == 0:
        break  # Sai do loop se n for igual a 0

    # Calcula a soma dos n inteiros consecutivos a partir de m
    soma = 0
    for i in range(m, m + n):
        soma += i

    # Escreve a soma na tela
    print("A soma dos {} inteiros consecutivos a partir de {} é {}.".format(n, m, soma))
