n = int(input())
n = n % (1440 * 60)
hh = (n - n % 3600) // 3600
a = n % 3600
mm = (a - a % 60) // 60
ss = n % 60
print(hh, str(mm // 10) + str(mm % 10), str(ss // 10) + str(ss % 10), sep = ':')