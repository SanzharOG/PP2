s = input()
i = s.find('f')
if i != -1:
    s = s.replace(s[i], '.', 1)
    j = s.rfind('f')
    if j != -1:
        print(i, j)
    else:
        print(i)