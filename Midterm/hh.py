n=int(input())
a={x for x in input().split()}
m=int(input())
b={x for x in input().split()}
j=0
print("Missed students:")
for i in a:
    if i not in b:
        print('-',end=' ')
        print(i)
print('Not in the group:')
for j in b:
    if j not in a:
        print('-',end=' ')
        print(j)





