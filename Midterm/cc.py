n=int(input())
c=str()
a=[]
a=input().split()
b={x for x in a}
if n==len(b):
    print("YES")
else: print("NO")