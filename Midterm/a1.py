def num():
    b=list(input().split())
    a=[]
    for i in range(0, len(b), 2):
        a.append(int(b[i]))
    print(*a)
num()