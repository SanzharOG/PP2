n = int(input())
plates = list(map(int, input().split()))[:n]
if n == 1:
    print('Clean:' + str(n))
    print('Dirty:0')
else:
    print('Clean:0\nDirty:' + str(n))