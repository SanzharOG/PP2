def wer():
    a=list(input().split())
    b=list(input().split())
    c=[]
    s = set.intersection(set(a), set(b))
    for i in s:
        c.append(int(i))
    c.sort()
    print(*c)
wer()
