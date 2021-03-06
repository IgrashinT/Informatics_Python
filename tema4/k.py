a, b = int(input()), int(input())
for i in range(a % 2 + a, b + 1, 2):
    print(i, end = ' ')