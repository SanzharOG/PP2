import re
s=input()
sub=input()
x=s[0]
i=1
for i in range(len(s)):
    x+=s[i]
    txt=re.search(sub, x)
    if txt==-1:
       print("(-1, -1)")
    m=txt.start()
    n=txt.end()
    print("("+str(m), str(n)+")")