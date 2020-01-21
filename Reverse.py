# Сделать ревер массива
# Пример 1
# 1 2 3 4 5
# 5 2 3 4 1
# 5 4 3 2 1
# 5 4 3 2 1

import random as r

n = int(input())
a = [r.randint(-10, 10) for i in range(n)]
print(*a)
for i in range(n // 2):
    a[i], a[-1 - i] = a[-1 - i], a[i]
print(*a)
