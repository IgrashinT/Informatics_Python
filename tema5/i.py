p = int(input())
x = int(input())
y = int(input())
k = int(input())
x = x * 100 + y
for i in range(k):
    x = int(x * ((p + 100) / 100))
print(x // 100, x % 100)