import re
from typing import Pattern
s=input()
x=[]
Pattern=r"[A-Z][a-z]"
x=re.findall(Pattern, s)
if x!=[]:
    print("Found a match!")
else: print("Not matched!")
