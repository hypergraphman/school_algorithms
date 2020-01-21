# Удаление элемента массива по индексу
# Пример 1
# 1 2 3 4 5
# 2
# 1 2 4 5 0

import random as r

n = int(input())
a = [r.randint(1, 10) for i in range(n)]
print(*a)
x = int(input())
for i in range(x, n - 1):
    a[i] = a[i + 1]
a[-1] = 0
print(*a)