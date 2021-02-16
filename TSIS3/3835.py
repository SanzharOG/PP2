a, mn = [int(i) for i in input().split()], 0
for i in a:
    if i > 0:
        mn = i
        break
for i in a:
    if i > 0 and mn > i: mn = i
print(mn)