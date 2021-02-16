a, res = [int(i) for i in input().split()], []
for i in a:
    if i != 0: res.append(i)
print(*res, end=' ')
for i in range(a.count(0)): print(0, end=' ')