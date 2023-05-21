"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

# Define as constantes para as taxas de bônus
TAXA_BONUS_1 = 0.1  # 10% de bônus para compras menores que 500.000
TAXA_BONUS_2 = 0.15  # 15% de bônus para compras iguais ou maiores que 500.000

# Lê os dados dos 150 clientes e calcula o valor do bônus para cada um
for i in range(150):
    nome = input("Digite o nome do cliente: ")
    compras = float(input("Digite o valor das compras do cliente no ano passado: "))

    if compras < 500000:
        bonus = compras * TAXA_BONUS_1
    else:
        bonus = compras * TAXA_BONUS_2

    # Exibe o resultado para o cliente atual
    print("O cliente {} receberá um bônus de R$ {:.2f}".format(nome, bonus))
