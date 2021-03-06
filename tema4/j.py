n = int(input())
s, t = '', ''
sum = 0
for i in range(n - 1):
    s += str(i + 1) + '*' + str(i + 2)
    if i != n - 2: s += '+'
    else: s += '='
    sum += (n - i) * (n - i - 1)
print(s, sum, sep = '')