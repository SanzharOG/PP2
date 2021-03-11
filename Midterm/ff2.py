n=int(input())
s=input()
t=''
for i in s:
    if ord(i)+n>90:
        t+=chr(ord(i)+n-26)
    else:t+=chr(ord(i)+n)
print(t)