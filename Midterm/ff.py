x=input().split()
a=int(x[0])
b=int(x[1])
cnt=0
while True:
    a=a*3
    b=b*2
    cnt+=1
    if a > b:
        break
print(cnt)  