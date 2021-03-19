import re
from typing import Pattern
string=input()
res=[]
Pattern='\d'
for i in range(len(string)):
    res=re.findall(Pattern,string)
a=''.join(res)
for i in range(len(a)):
    l=a[i]
    if l in a[i+1:]:
        print(l)
        break
