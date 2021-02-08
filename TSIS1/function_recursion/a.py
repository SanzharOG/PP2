def Distance(x1, y1, x2, y2):
    return(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(Distance(x1, y1, x2, y2))