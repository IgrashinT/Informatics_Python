import math as mt
n = float(input())
m = int(10 * (n - int(n)))
if m >= 5:
    print(mt.ceil(n))
else:
    print(mt.floor(n))