s=input().split()
max=0

for i in range(len(s)):
    if len(s[i])>max:
        max=len(s[i])
        x=s[i]
print(x)
print(max)

    