sin, n = {}, int(input())
for i in range(n):
    s1, s2 = map(str, input().split())
    sin[s1] = s2
    sin[s2] = s1
x = str(input())
print(sin[x])