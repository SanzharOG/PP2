s = input()
i = s.find(' ')
print(s[i+1:], end = ' ')
print(s[:i])