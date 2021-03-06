n = int(input())
n = n % 1440
print((n - n % 60) // 60 ,n % 60)