"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

linhas = int(input())
desenho, espaco = "%", " "
for i in range(0, linhas + 1, 2):
    print(espaco * (2 + linhas - i) + desenho * (1 + 2 * i))
for i in range(linhas, -2, -2):
    print(espaco * (1 + linhas - i) + desenho * (3 + 2 * i))
if linhas % 2 == 0:
    print(espaco * (2 + linhas - i) + desenho)


n = 1
desenho = "%"
espaco = " "

while linhas >= n:
    formato = espaco * (linhas - n) + desenho * n
    print(formato)
    n += 1
