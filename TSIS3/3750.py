a, b = [int(i) for i in input().split()], [int(i) for i in input().split()]
s = set.intersection(set(a), set(b))
print(len(s))