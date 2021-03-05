def wer():
    n, m =input().split()
    f=set()
    r=set()
    for i in range(int(n)):
         f.add(int(input()))
    for i in range(int(m)):
         r.add(int(input()))
    print(len(f.intersection(r)))
    print(*sorted(f.intersection(r)))
    print(len(f.difference(r)))
    print(*sorted(f.difference(r)))
    print(len(r.difference(f)))
    print(*sorted(r.difference(f)))
wer()
