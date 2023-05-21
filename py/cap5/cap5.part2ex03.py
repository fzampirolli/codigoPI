"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def geraVetor(v1):
    vetorV1 = [int(i) for i in v1.split(" ") if i]

    return vetorV1


def geraVetorContador(vetorV1):
    contador = {}
    for i in vetorV1:
        if not i in contador:
            contador[i] = 1
        else:
            contador[i] += 1

    return contador


v1 = input()
vetorV1 = geraVetor(v1)
contador = geraVetorContador(vetorV1)

print(contador)
