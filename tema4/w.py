a, b, c, d = int(input()), int(input()), int(input()), int(input())
if c == 0:
    x = d
else:
    if d % c == 0:
        x = 1
    else: x = d % c
for i in range(a % x + a, b + 1, x):
    print(i, end = ' ')