a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a - 1 == c and (b + 1 == d or b == d or b - 1 == d)) or (a == c and(b == d or b + 1 == d or b - 1 == d)) or (a + 1 == c and (b + 1 == d or b == d or b - 1 == d)): print("YES")
else: print("NO")
