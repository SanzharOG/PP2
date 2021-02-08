n = int(input())
i = 0
while True:
    if 2 ** i == n:
        print('YES')
        exit()
    if 2 ** i > n:
        break
    i += 1
print('NO')