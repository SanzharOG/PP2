import re
txt=input()
word=input()
x=re.search(word,txt)
if x: print("First time",word, "occured in position:", x.start())
else: print("Not found")