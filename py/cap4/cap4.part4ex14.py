"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

# Define as constantes para os limites de notas e conceitos
LIMITE_D = 4.9
LIMITE_C = 6.9
LIMITE_B = 8.9

# Lê os dados dos 75 alunos e calcula o conceito final para cada um
for i in range(75):
    matricula = input("Digite o número de matrícula do aluno: ")
    nota = float(input("Digite a nota numérica final do aluno: "))

    # Calcula o conceito final de acordo com a nota do aluno
    if nota >= 0 and nota <= LIMITE_D:
        conceito = "D"
    elif nota <= LIMITE_C:
        conceito = "C"
    elif nota <= LIMITE_B:
        conceito = "B"
    else:
        conceito = "A"

    # Exibe o resultado para o aluno atual
    print("O aluno de matrícula {} recebeu o conceito {}".format(matricula, conceito))
