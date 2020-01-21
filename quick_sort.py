import random as r


def quick_sort(n_start, n_end):
    global count
    if n_start < n_end:
        left = n_start
        right = n_end
        x = a[(left + right) // 2]
        while left <= right:
            while a[left] < x:
                left += 1
                count += 1
            while a[right] > x:
                right -= 1
                count += 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
                count += 2
        quick_sort(n_start, right)
        quick_sort(left, n_end)


n = 100000
a = [r.randint(1, n) for i in range(n)]
# print(*a)
count = 0
quick_sort(0, n - 1)
print(count)
# print(*a)