n = int(input())
if n >= 86400:
    while n >= 86400:
        n = n - 86400
hours = n // 3600
minutes = (n % 3600) // 60
seconds = (n % 3600) % 60
if (minutes < 10) and (seconds < 10):
    print(hours, end = ':0')
    print(minutes, end = ':0')
    print(seconds)
elif (minutes >= 10) and (seconds < 10):
    print(hours, end = ':')
    print(minutes, end = ':0')
    print(seconds)
elif (minutes < 10) and (seconds >= 10):
    print(hours, end = ':0')
    print(minutes, end = ':')
    print(seconds)
else:
    print(hours, end = ':')
    print(minutes, end = ':')
    print(seconds)