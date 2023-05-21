"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
Código gerado pelo ChatGPT
"""

temperaturas = []

# Lê a temperatura média de cada dia do ano
for i in range(1, 6):
    temperatura = float(
        input("Digite a temperatura média do dia {} (em graus Celsius): ".format(i))
    )
    temperaturas.append(temperatura)

# Calcula a menor e a maior temperatura do ano
menor_temperatura = min(temperaturas)
maior_temperatura = max(temperaturas)

# Calcula a temperatura média anual
temperatura_media = sum(temperaturas) / len(temperaturas)

# Calcula o número de dias no ano em que a temperatura foi inferior à média anual
dias_temperatura_inferior_media = 0
for temperatura in temperaturas:
    if temperatura < temperatura_media:
        dias_temperatura_inferior_media += 1

# Imprime os resultados
print("A menor temperatura do ano foi: {:.2f} graus Celsius".format(menor_temperatura))
print("A maior temperatura do ano foi: {:.2f} graus Celsius".format(maior_temperatura))
print("A temperatura média anual foi: {:.2f} graus Celsius".format(temperatura_media))
print(
    "O número de dias no ano em que a temperatura foi inferior à média anual foi: {}".format(
        dias_temperatura_inferior_media
    )
)
