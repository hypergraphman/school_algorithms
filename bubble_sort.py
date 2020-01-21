import random as r

n = 100000
count = 0
a = [r.randint(1, n) for i in range(n)]
# print(*a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]


print(count)
# print(*a)
