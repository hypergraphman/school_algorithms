# Циклический сдвиг влево
# Пример 1
# 1 2 3 4 5
# 2 3 4 5 1

import random as r

n = int(input())
a = [r.randint(-10, 10) for i in range(n)]
print(*a)
t = a[0]
for i in range(n - 1):
    a[i] = a[i + 1]
a[-1] = t
print(*a)