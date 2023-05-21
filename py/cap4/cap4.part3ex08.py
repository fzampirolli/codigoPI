"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

rafa = 1.50
ze = 1.10
anos = 0
while rafa > ze:
    rafa += 0.02
    ze += 0.03
    anos += 1
print(anos, "anos")
