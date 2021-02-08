def MinFind(x1, y1, x2, y2):
    return(min(min(x1, y1), min(x2, y2)))

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
print(MinFind(x1, y1, x2, y2))