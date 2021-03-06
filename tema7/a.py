import math as mt
n = int(input())
a = 1
while a <= n:
    if mt.sqrt(a) == int(mt.sqrt(a)):
        print(a, end = ' ')
    a += 1