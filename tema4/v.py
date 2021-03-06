a, b = int(input()), int(input())
for i in range(a, b + 1):
    for j in range(0, 10):
        if str(i).count(str(j)) == 3:
            print(i)