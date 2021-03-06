import math
'''
a, b, c = float(input()), float(input()), float(input())
d = b * b - 4 * a * c
if d > 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    y = (-b - math.sqrt(d) ) / (2 * a)
    print(2, min(x, y), max(x, y))
elif d == 0:
    print(1, -b / (2 * a))
else:
    print(0)
'''
a, b, c = float(input()), float(input()), float(input())
l = []
for i in range(-10000, 10001):
    if a * (i * i) + b * i + c == 0:
        l.append(i)
if len(l) > 2:
    print(3)
elif len(l) == 2:
    print(2, l[0], l[1])
elif len(l) == 1:
    print(1, l[0])
else:
    print(0)
