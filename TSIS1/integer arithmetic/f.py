v, t = int(input()), int(input())
s = v * t
if (s <= 108) and (v > 0):
    print(s)
if (v > 0) and (s > 108):
    while s >= 109:
        s = s - 109
    print(s)
if (v < 0) and (s > -109):
    while (s <= 109) and (s < 0):
        s = 109 + s
    print(s)
if (v < 0) and (s < -109):
    while (s <= 109) and (s < 0):
        s = 109 + s
    print(s)