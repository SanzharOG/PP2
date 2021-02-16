a, b, res = [int(i) for i in input().split()], [int(i) for i in input().split()], []
s = set.intersection(set(a), set(b))
for i in s: res.append(i)
res.sort()
print(*res)