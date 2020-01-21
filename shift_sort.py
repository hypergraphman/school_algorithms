import random as r

n = 10
a = [r.randint(1, 20) for i in range(n)]
print(*a)

for i in range(1, n):
    j = i
    while j > 0 and a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1

print(*a)