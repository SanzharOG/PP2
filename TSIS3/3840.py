a = [int(i) for i in input().split()]
n = len(a) - 1
for i in range(len(a)):
    if i >= n: break
    a[i], a[n] = a[n], a[i]
    n -= 1
print(*a)