import re
from typing import Pattern
s=input()
x=[]
Pattern=r'\w'
x=re.findall(Pattern, s)
if len(x)==len(s):
    print("Found a match!")
else: print("Not matched!")