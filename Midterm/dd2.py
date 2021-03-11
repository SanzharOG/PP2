from sys import stdin

inp = str(stdin.read()).split()
my_dict, ans = {}, []
for i in inp:
    my_dict[i] = my_dict.get(i, 1) + 1
for i in my_dict:
    if my_dict[i] % 2 != 0:
        ans.append(i)
for i in sorted(set(ans)):
    print(i)