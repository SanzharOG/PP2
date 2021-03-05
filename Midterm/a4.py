def num():
    b=list(input().split())
    a=[]
    for i in range(len(b)):
        if(int(b[i])!=0):
            a.append(b[i])   
    x=len(b)-len(a)
    for i in range(x):
        a.append(0)
    print(*a)
num()