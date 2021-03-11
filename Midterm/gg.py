import re
txt=input()
t=input()
s=input()
f=input()
txt=txt.replace(t, s)
x=re.findall(f, txt)
print(len(x))