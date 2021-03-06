import math as mt
def IsPointInSquare(x, y):
        return(x + y <= 2.0 and x <= 1 and y <= 1)
x, y = float(input()), float(input())
x = abs(x)
y = abs(y)
if IsPointInSquare(x, y): print("YES")
else: print("NO")
