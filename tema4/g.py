n, k = int(input()), int(input())
x = 1
m = n - k
for i in range(n, m, -1):
    x *= i
for i in range(2, k + 1):
    x /= i
print(int(x))