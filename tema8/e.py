import math as mt
def IsPointInCircle(x, y):
    return((x + 1) ** 2 + (y - 1) ** 2 <= 4)
x, y = float(input()), float(input())
print("YES") if IsPointInCircle(x, y) else print("NO")