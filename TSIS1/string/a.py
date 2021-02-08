s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end = '')
print()
for i in range(len(s)):
    if i % 2 != 0:
        print(s[i], end = '')
print()
print(s[::-1])
for i in range(len(s)-1, -1, -2):
    print(s[i], end = '')
print()
print(len(s))