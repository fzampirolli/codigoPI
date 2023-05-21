"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

import math  # Importa o módulo math para usar a função sqrt()

contador = 0  # Inicializa o contador de linhas

# Escreve o cabeçalho da tabela
print("{:<10} {:<10} {:<10} {:<10}".format("Valor", "Quadrado", "Cubo", "Raiz"))

# Lê valores até que o usuário digite um valor negativo
while True:
    valor = float(input("Digite um valor (negativo para encerrar): "))
    if valor < 0:
        break  # Sai do loop se um valor negativo for lido

    # Calcula o quadrado, o cubo e a raiz quadrada do valor
    quadrado = valor**2
    cubo = valor**3
    raiz = math.sqrt(valor)

    # Escreve uma linha da tabela com os valores calculados
    print("{:<10} {:<10} {:<10} {:<10}".format(valor, quadrado, cubo, raiz))

    # Incrementa o contador de linhas
    contador += 1

    # Escreve o cabeçalho novamente a cada 20 linhas
    if contador % 20 == 0:
        print("{:<10} {:<10} {:<10} {:<10}".format("Valor", "Quadrado", "Cubo", "Raiz"))
