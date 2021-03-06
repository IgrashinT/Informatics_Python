s = int(input())
x = s - (s // 1000) * 1000
z = s // 1000
y = x // 100
x = x - (x // 100) * 100
x = x - z % 10
print(x - (y % 10) * 10 + 1)