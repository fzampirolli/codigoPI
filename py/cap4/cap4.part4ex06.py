"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

while True:
    cod = int(input())
    if cod < 0:
        break
    p1, p2, p3 = int(input()), int(input()), int(input())
    m = (p1 * 4 + 3 * (p2 + p3)) / 10
    print("cod={} p1={} p2={} p3={} m={:.2f}".format(cod, p1, p2, p3, m))
    if m >= 5:
        print("aprovado")
    else:
        print("reprovado")
