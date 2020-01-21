import random as r

n = 4
m = 4
a = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(r.randint(0, 9))
    print(*row, sep='\t')
    a.append(row)
print('-----------')
# Сумма всех эл-тов матрицы
summa = 0
for i in range(n):
    for j in range(m):
        summa += a[i][j]
print(summa)
# Сумма каждой строки матрицы
for i in range(n):
    summa = 0
    for j in range(m):
        summa += a[i][j]
    print(summa)