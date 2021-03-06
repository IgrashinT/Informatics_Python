n = int(input())
a = 0.5
while a < n:
    if a * 2 == n:
        print("YES")
        break
    a *= 2
else: print("NO")