n=int(input())
a={x for x in input().split()}
m=int(input())
b={x for x in input().split()}
print("Missed students:")
for i in a:
    if b.find(a[i])==-1:
        print("-", i)





