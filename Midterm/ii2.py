n=int(input())
a=input().split()
x=''
for i in range(len(a)-1):
    if int(a[i])>int(a[i+1]):
        x="NO"
if x!="NO" or x=='':
   print("Interesting")
else: print("Not interesting")