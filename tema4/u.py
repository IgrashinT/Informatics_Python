n, m = int(input()), int(input())
for i in range(n, m + 1):
    s = str(i)
    if s[0] == s[3] and s[1] == s[2]:
        print(i)