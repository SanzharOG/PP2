h, a, b = int(input()), int(input()), int(input())
print((h // (a - b) - (a - (h % (a - b))) // (a - b)) + 1)