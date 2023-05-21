"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

n_masc = n_fem = alt_total = alt_fem = 0
for i in range(1, 3):
    altura = float(input("Altura da %dº pessoa em metros: " % i))
    sexo = int(input("Digite 0 para sexo masculino e 1 para feminino: "))
    if i == 1:
        menor, maior = altura, altura
    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura
    if sexo == 0:
        n_masc += 1
    if sexo == 1:
        n_fem += 1
        alt_fem += altura
    alt_total += altura

print("Menor Altura:", menor)
print("Maior Altura:", maior)
print("Média da altura das mulheres:", alt_fem / n_fem)
print("Média da altura da população:", alt_total / i)
print("Percentual de homens: %.2f" % (n_masc * 100 / i))
