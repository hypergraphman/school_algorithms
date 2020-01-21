# Найти три минимума за один проход по циклу
#  Пример 1
#  8 1 7 2 6 3 4 5
#  1 2 3
#  Пример 2
#  8 1 7 2 6 1 4 5
#  1 1 2
import random as r
import math

n = int(input())
a = [r.randint(-10, 10) for i in range(n)]
print(*a)
m1 = m2 = m3 = math.inf
for el in a:
    if el < m1:
        m3, m2, m1 = m2, m1, el
    elif el < m2:
        m3, m2 = m2, el
    elif el < m3:
        m3 = el
print(m1, m2, m3)