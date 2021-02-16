res, cnt = [], {}
while True:
    s = input().split()
    for i in s:
        if i in cnt.keys(): cnt[i] += 1
        else: cnt[i] = 1
for i, j in cnt.items():
    res.append((j, i))
res.sort()
res.reverse()
'''s, b = res[0][0], res[len(res)-1][0]
while True:
    for i in range(len(res)):
        if res[i][0] < b: continue
        elif res[i][0] > b: break
        else: print(res[i][1])
    b -= 1
    if b < s: break'''
for i in res:
    print(i)