n=int(input())
str=''
str1=''
a=input().split()
m=int(input())
for i in range(m):
    str+=a[i]
for i in range(m, n):
    str1+=a[i]
if str=='':
    str=0
if str1=='':
    str1=0
print(int(str)*int(str1))