"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

a = int(input())
fat = 1
texto = str(a) + "!="
while a > 0:
    if a == 1:
        texto += str(a)
    else:
        texto += str(a) + "X"
    fat *= a
    a -= 1
print(texto + "=" + str(fat))
