import re
from typing import Pattern
n=int(input())
res=[]
pattern='^[-+]?[0-9]*\.[0-9]+$'
for i in range(n):
    string=input()
    if len(re.findall(pattern,string))==0:
        res.append("False")
    else:
        if string==re.findall(pattern,string)[0]:
           res.append("True")
        else:
            res.append("False")
for i in res:
    print(i)