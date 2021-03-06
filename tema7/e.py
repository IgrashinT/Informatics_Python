n = int(input())
i = 0
a = 0.5
while True:
    if 2 * a >= n:
        print(i)
        break
    a *= 2
    i += 1