"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

# Lendo o vetor de 20 números
vetor = []
for i in range(20):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

# Lendo o número a ser verificado
num = int(input("Digite um número para verificar se existe no vetor: "))

# Verificando se o número existe no vetor
if num in vetor:
    # Gerando um novo vetor sem o número
    novo_vetor = [x for x in vetor if x != num]
    print(
        f"O número {num} foi encontrado no vetor e foi removido. O novo vetor é: {novo_vetor}"
    )
else:
    print(f"O número {num} não foi encontrado no vetor.")
