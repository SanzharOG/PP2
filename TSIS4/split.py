import re
from typing import Pattern
Pattern='[0-9]+'
string=input()
res=[]
res=re.findall(Pattern, string)
for i in res:
    print(i)