m, n = map(int, input().split())
a_m, b_n, res = [], [], []
for i in range(m): a_m.append(int(input()))
for i in range(n): b_n.append(int(input()))
s = set.intersection(set(a_m), set(b_n))
for i in s: res.append(i)
res.sort()
a_x, b_x = [], []
for i in a_m:
    if i not in res: a_x.append(i)
for i in b_n:
    if i not in res: b_x.append(i)
a_x.sort()
b_x.sort()
print(len(res))
print(*res)
print(len(a_x))
print(*a_x)
print(len(b_x))
print(*b_x)