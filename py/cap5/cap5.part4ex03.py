"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import numpy as np

v = np.random.randint(2, size=10)
print(*v)
r = 0
for i in range(len(v) - 1):
    r = r or (v[i] and v[i + 1])
print(r)
