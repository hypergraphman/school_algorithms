# Циклический сдвиг вправо
# Пример 1
# 1 2 3 4 5
# 5 1 2 3 4

import random as r

n = int(input())
a = [r.randint(1, 10) for i in range(n)]
print(*a)
t = a[-1]
for i in range(n - 1, 0, -1):
    a[i] = a[i - 1]
a[0] = t
print(*a)