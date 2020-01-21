import random as r

n = 2
m = 3
a = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(r.randint(0, 9))
    print(*row, sep='\t')
    a.append(row)
print('-----------')
b = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(r.randint(0, 9))
    print(*row, sep='\t')
    b.append(row)
print('-----------')
c = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(a[i][j] + b[i][j])
    print(*row, sep='\t')
    c.append(row)
print('-----------')