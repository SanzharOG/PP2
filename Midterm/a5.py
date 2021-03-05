def num():
    b=list(input().split())
    k=int(input()) % len(b)
    print(*(b[-k:]+b[:-k]))
num()