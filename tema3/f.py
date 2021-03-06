a, b, c = int(input()), int(input()), int(input())
a1 = max(a, b, c)
b1 = min(a, b, c)
c1 = a + b + c - a1 - b1
if b1 + c1 > a1: print("YES")
else: print("NO")