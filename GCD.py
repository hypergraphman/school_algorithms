# медленный
a, b = map(int, input().split())

while a != b:
    if a < b:
        b -= a
    else:
        a -= b

print('gcd:', a)

# быстрый
a, b = map(int, input().split())

while b:
    a, b = b, a % b

print('gcd:', a)