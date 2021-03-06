N = int(input())
a = N
b = int(N ** (1 / 2))
for i in range(2, b+1):
        if N % i == 0:
            a = i
            break
print(a)