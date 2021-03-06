a = int(input())
b = int(input())
c = int(input())
a = (a - a % 2) // 2 + a % 2
b = (b - b % 2) // 2 + b % 2
c = (c - c % 2) // 2 + c % 2
print(a  + b + c)