"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

# Cria uma lista vazia para armazenar os dados das cidades
cidades = []

# Lê os dados das 200 cidades e adiciona à lista
for i in range(200):
    codigo = int(input("Digite o código da cidade: "))
    estado = input("Digite o estado da cidade: ")
    veiculos = int(input("Digite o número de veículos de passeio da cidade em 1992: "))
    acidentes = int(
        input(
            "Digite o número de acidentes de trânsito com vítimas da cidade em 1992: "
        )
    )

    cidade = (codigo, estado, veiculos, acidentes)
    cidades.append(cidade)

# Calcula o maior e o menor índice de acidentes de trânsito e as cidades correspondentes
maior_indice = 0
menor_indice = float("inf")
cidade_maior_indice = None
cidade_menor_indice = None
for cidade in cidades:
    indice = cidade[3] / cidade[2]
    if indice > maior_indice:
        maior_indice = indice
        cidade_maior_indice = cidade
    if indice < menor_indice:
        menor_indice = indice
        cidade_menor_indice = cidade

# Escreve os resultados na tela
print(
    "Maior índice de acidentes de trânsito: {:.2f} - cidade {} ({})".format(
        maior_indice, cidade_maior_indice[0], cidade_maior_indice[1]
    )
)
print(
    "Menor índice de acidentes de trânsito: {:.2f} - cidade {} ({})".format(
        menor_indice, cidade_menor_indice[0], cidade_menor_indice[1]
    )
)

# Calcula a média de veículos nas cidades brasileiras
soma_veiculos = sum(cidade[2] for cidade in cidades)
media_veiculos = soma_veiculos / len(cidades)

# Escreve o resultado na tela
print("Média de veículos nas cidades brasileiras: {:.2f}".format(media_veiculos))

# Calcula a média de acidentes com vítimas entre as cidades do Rio Grande do Sul
cidades_rs = [cidade for cidade in cidades if cidade[1] == "RS"]
soma_acidentes_rs = sum(cidade[3] for cidade in cidades_rs)
media_acidentes_rs = soma_acidentes_rs / len(cidades_rs)

# Escreve o resultado na telaprint("Média de acidentes com vítimas entre as cidades do Rio Grande do Sul: {:.2f}".format(media_acidentes_rs))
