import random as r

n = 4
m = 5
a = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(r.randint(1, 9))
    print(*row, sep='\t')
    a.append(row)
print('-----------')
# Поиск последнего минимального элемента в матрице по индексам
mini = 0
minj = 0
for i in range(n):
    for j in range(m):
        if a[mini][minj] >= a[i][j]:
            mini = i
            minj = j
print(a[mini][minj], mini, minj)