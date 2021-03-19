import re
from typing import Pattern
string=input()
res=re.split('[,.]',string)
for i in res:
    print(i)