s=input()
a=input().split()
x0=0
y0=0
z=''
x=int(a[0])
y=int(a[1])

for i in range(len(s)):
    if x0==x and y0==y:
            z="sasa"
    if s[i]=="L":
        x0=x0-1
    if s[i]=="R":
        x0=x0+1
    if s[i]=="U":
        y0=y0+1
    if s[i]=="D":
        y0=y0-1
    
if z!="sasa":
    print("Missed")
if z=="sasa":
    print("Passed")
    