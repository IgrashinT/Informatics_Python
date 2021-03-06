n = int(input())
l = []
for i in range(1, 6):
    for j in range(1, 10):
        if (j >= 4 and j <= 6 and i == 1):
            if j % 2 == 0:
                l[i][j] = '_'
            else: l[i][j] = '~'
