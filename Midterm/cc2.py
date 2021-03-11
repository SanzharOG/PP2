n=int(input())
a=sorted(set(list(map(int, input().strip().split()))))
for i in range(1, len(a)+1):
    print(i, a[i-1])