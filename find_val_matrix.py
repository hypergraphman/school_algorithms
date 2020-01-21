import random as r

n = 4
m = 5
a = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(r.randint(1, 99))
    print(*row, sep='\t')
    a.append(row)
print('-----------')
# Поиск первого минимального элемента в матрице
minimum = 100
for i in range(n):
    for j in range(m):
        if minimum > a[i][j]:
            minimum = a[i][j]
print(minimum)

# Поиск первого минимального элемента в каждой строке матрице
for i in range(n):
    minimum = 100
    for j in range(m):
        if minimum > a[i][j]:
            minimum = a[i][j]
    print(minimum)