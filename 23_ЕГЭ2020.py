import itertools


def check(x, y):
    for i in range(len(x) - 1):
        for j in range(len(y) - 1):
            if not (not(x[i] and y[j]) or (x[i + 1] and y[j + 1])):
                return False
    return True


x = [i for i in itertools.product([True, False], repeat=6)]
y = [i for i in itertools.product([True, False], repeat=7)]
xy = list(itertools.product(x, y))

count = 0
for x, y in xy:
    count += (0, 1)[check(x, y)]

print(count)
