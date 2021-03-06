n = int(input())
for i in range(100, 1000):
    if i % 10 + (i // 10) % 10 + i // 100 == n:
        print(i)