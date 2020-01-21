import random as r

n = 10
a = [r.randint(1, 20) for i in range(n)]
print(*a)

for i in range(n - 1):
    min_j = i
    for j in range(i + 1, n):
        if a[min_j] > a[j]:
            min_j = j
    a[min_j], a[i] = a[i], a[min_j]


print(*a)