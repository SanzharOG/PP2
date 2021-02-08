n = int(input())
if n > 1440:
    while n > 1440:
        n = n - 1440
hours = n // 60
minutes = n % 60
if hours == 24:
    hours = 0
print(hours, minutes)