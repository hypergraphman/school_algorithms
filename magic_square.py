# Строим магический квадрат (квадратная матрица размера N на N заполненная цифрами
# от 1 до N*N включительно таким образом, что сумма каждого столбца, каждой строки
# и обеих диагоналей равна n * (n ** 2 + 1) // 2)
# код не красивый, нужно отредактировать


def is_mag_square(m, n):
    t = sum(m[0])
    sum_d1 = 0
    sum_d2 = 0
    for i in range(n):
        if t != sum(m[i]):
            return False
        sum_column = 0
        for j in range(n):
            sum_column += m[j][i]
        if t != sum_column:
            return False
        sum_d1 += m[i][i]
        sum_d2 += m[i][n - 1 - i]
    if t != sum_d1 or t != sum_d2 or t != n * (n ** 2 + 1) // 2:
        return False

    return True


def gen_mag_square(N):
    d = {}
    Y, X, y, x = 0, 1 - N, 0, 1 - N
    for i in range(1, N ** 2 + 1):
        d[y, x] = i
        y += 1
        x += 1
        if i % N == 0:
            Y -= 1
            X += 1
            y, x = Y, X

    for i in range(N // 2 + 1, N):
        for j in range(-(N // 2 - 1), N // 2):
            if (i, j) in d:
                d[(i - N, j)] = d[(i, j)]
            if (-i, j) in d:
                d[(N - i, j)] = d[(-i, j)]
            if (j, i) in d:
                d[(j, i - N)] = d[(j, i)]
            if (j, -i) in d:
                d[(j, N - i)] = d[(j, -i)]

    ans = []
    for y in range(N // 2, -(N // 2 + 1), -1):
        row = []
        for x in range(-(N // 2), N // 2 + 1):
            row.append(d[(y, x)])
        ans.append(row)

    return ans


def gen_mag4k_square(N):
    q = 1
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i < N // 2 and j < N // 2:
                if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                    ans[N - 1 - i][N - 1 - j] = q
                    q += 1
                else:
                    ans[i][j] = q
                    q += 1
            if i < N // 2 and j >= N // 2:
                if i % 2 == 0 and j % 2 != 0 or i % 2 != 0 and j % 2 == 0:
                    ans[N - 1 - i][N - 1 - j] = q
                    q += 1
                else:
                    ans[i][j] = q
                    q += 1
            if i >= N // 2 and j < N // 2:
                if i % 2 == 0 and j % 2 != 0 or i % 2 != 0 and j % 2 == 0:
                    ans[N - 1 - i][N - 1 - j] = q
                    q += 1
                else:
                    ans[i][j] = q
                    q += 1
            if i >= N // 2 and j >= N // 2:
                if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                    ans[N - 1 - i][N - 1 - j] = q
                    q += 1
                else:
                    ans[i][j] = q
                    q += 1
    return ans


def gen_mag4k_plus2_square(N):
    # 0
    ans = gen_mag4k_square(N)
    # 1
    i = N // 2 - 1
    j = N // 2 - 2
    ans[i][j + 1], ans[i][j + 2] = ans[i][j] + 1, ans[i][j] + 2
    i += 1
    ans[i][j + 1], ans[i][j + 2] = ans[i][j] + 1, ans[i][j] + 2
    # 2
    i = N // 2
    j = 0
    q = 1 + N * (N // 2 - 1)
    ans[i][j] = q
    ans[i][j + N // 2 + 1] = q + N // 2 + 1
    ans[i][-1] = q + N - 1

    q = N // 2
    ans[j][i] = q
    ans[j + N // 2 + 1][i] = q + N * (N // 2 + 1)
    ans[-1][i] = q + N * (N - 1)
    # 3
    q1 = N // 2 + 2 + N * (N // 2)
    q2 = N // 2 + 1 + N * (N // 2 + 1)
    i = N // 2 - 1
    j = N // 2 + 1
    ans[i][j] = q1
    ans[j][i] = q2
    # 4
    ans[1][-1] = N + N * (N - 2)
    ans[1 + N // 2][-1] = N + N * (N // 2 - 2)
    for i in range(3, N // 2 - 1, 2):
        ans[i][-1] = ans[1][-1] - (i - 1) * N
        ans[i + N // 2][-1] = ans[1][-1] - (i + N // 2 - 1) * N
        ans[i - 1][-1] = 1 + N * (i - 1)
        ans[i + N // 2 - 1][-1] = 1 + N * (i + N // 2 - 1)
    # 5
    ans[-1][1] = N - 1 + N * (N - 1)
    ans[-1][1 + N // 2] = N // 2 - 1 + N * (N - 1)
    for j in range(3, N // 2 - 1, 2):
        ans[-1][j] = ans[-1][1] - (j - 1)
        ans[-1][j + N // 2] = ans[-1][1 + N // 2] - (j - 1)
        ans[-1][j - 1] = j
        ans[-1][j + N // 2 - 1] = j + N // 2

    return ans


N = int(input())
if N % 2 != 0:
    M = gen_mag_square(N)
elif N % 4 == 0:
    M = gen_mag4k_square(N)
else:
    M = gen_mag4k_plus2_square(N)

# if is_mag_square(M, N):
#     print("YES")
# else:
#     print("NO")

for i in range(len(M)):
    print(*M[i])
