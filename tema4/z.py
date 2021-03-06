'''
max_value = 0
sum = 0
overall_sum = 0
for i in range(int(input()) - 1):
    x = int(input())
    max_value = max(max_value, x)
    sum += x
for i in range(1, max_value + 1):
    overall_sum += i
if overall_sum - sum == 0:
    print(overall_sum - sum + (max_value + 1))
else: print(overall_sum - sum)
'''
n = int(input())
sum = n * (n + 1) // 2
for i in range(n - 1):
    sum -= int(input())
print(sum)