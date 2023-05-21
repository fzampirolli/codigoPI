"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

# Define as constantes para as categorias de sexo, cor dos olhos e cor dos cabelos
SEXO_MASCULINO = "M"
SEXO_FEMININO = "F"
COR_OLHOS_AZUIS = "A"
COR_OLHOS_VERDES = "V"
COR_OLHOS_CASTANHOS = "C"
COR_CABELOS_LOUROS = "L"
COR_CABELOS_CASTANHOS = "C"
COR_CABELOS_PRETOS = "P"

# Cria uma lista vazia para armazenar os dados das pessoas
pessoas = []

# Lê os dados das 500 pessoas e adiciona à lista
for i in range(5):
    sexo = input("Digite o sexo da pessoa (M ou F): ")
    cor_olhos = input("Digite a cor dos olhos da pessoa (A, V ou C): ")
    cor_cabelos = input("Digite a cor dos cabelos da pessoa (L, C ou P): ")
    idade = int(input("Digite a idade da pessoa: "))

    pessoa = (sexo, cor_olhos, cor_cabelos, idade)
    pessoas.append(pessoa)

# Calcula a maior idade do grupo
maior_idade = 0
for pessoa in pessoas:
    if pessoa[3] > maior_idade:
        maior_idade = pessoa[3]

# Calcula a quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos louros
quantidade_mulheres_18_35_verdes_louros = 0
for pessoa in pessoas:
    if (
        pessoa[0] == SEXO_FEMININO
        and 18 <= pessoa[3] <= 35
        and pessoa[1] == COR_OLHOS_VERDES
        and pessoa[2] == COR_CABELOS_LOUROS
    ):
        quantidade_mulheres_18_35_verdes_louros += 1

# Escreve os resultados na tela
print("Maior idade do grupo: {}".format(maior_idade))
print(
    "Quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos louros: {}".format(
        quantidade_mulheres_18_35_verdes_louros
    )
)
