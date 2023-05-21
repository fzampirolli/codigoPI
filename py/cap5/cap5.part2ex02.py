"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

existe = 0


def geraVetor(notas):
    vetorNotas = [int(i) for i in notas.split(" ") if i]

    return vetorNotas


def encontraMenor(vetorNotas):
    notaMenor = vetorNotas[0]
    for i in range(1, len(vetorNotas)):
        if vetorNotas[i] < notaMenor:
            notaMenor = vetorNotas[i]

    return notaMenor


def verificaRepeticao(notaMenor, vetorNotas):
    global existe
    for i in range(len(vetorNotas)):
        if notaMenor == vetorNotas[i]:
            existe += 1


notas = input()
vetorNotas = geraVetor(notas)
notaMenor = encontraMenor(vetorNotas)
verificaRepeticao(notaMenor, vetorNotas)

print(f"A menor nota da turma é: {notaMenor}\nEle se repete {existe} vezes")
