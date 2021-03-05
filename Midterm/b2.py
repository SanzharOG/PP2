def wer():
    a=list(input().split())
    b=list(input().split())
    s = set.intersection(set(a), set(b))
    print(len(s))
wer()