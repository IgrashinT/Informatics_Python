n = int(input())
cnt = 0
a = True
for i in range(1, n + 1):
    if a == False:
        break
    for j in range(i):
        if cnt == n:
            a = False
            break
        print(i, end = ' ')
        cnt += 1