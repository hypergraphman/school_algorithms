import random as r
import math

n = int(input())
a = [r.randint(0, 10) for i in range(n)]
c = [0] * 11
for i in range(n):
    c[a[i]] += 1
m = -math.inf
indm = -1
for i in range(len(c)):
    if c[i] > m:
        m = c[i]
        indm = i
print(indm)

print(c.index(max(c)))