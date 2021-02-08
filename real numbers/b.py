n = input()
i = n.find('.')
if i == -1:
    print(0)
else:
    print(n[i+1:i+2])