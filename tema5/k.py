import math

a, b, c = float(input()), float(input()), float(input())
d = b * b - 4 * a * c
if d > 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    y = (-b - math.sqrt(d) ) / (2 * a)
    print(min(x, y), max(x, y))
elif d == 0:
    print(-b / (2 * a))
else:
    pass
