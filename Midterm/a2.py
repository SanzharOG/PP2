def num():
    b=list(input().split())
    a=[]
    for i in range(len(b)):
        if(int(b[i])>0):
            a.append(int(b[i]))
            a.sort()
    print(a[0])
num()