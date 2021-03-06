a, b, c = int(input()), int(input()), int(input())
s = (a * 100 + b) * c
print((s - s % 100) // 100, s % 100)
print()