n = int(input())
sum = 0
x = 1
for i in range(1, n + 1):
    for i in range(1, i + 1):
        x *= i
    sum += x
    x = 1
print(sum)