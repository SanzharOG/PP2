a = list(input().split())
k = int(input()) % len(a)
print(*(a[-k:] + a[:-k]))