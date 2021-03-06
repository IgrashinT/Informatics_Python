p = 0
j = 0
for i in range(20):
    if i % 2 != 0:
        p += ((-1) ** j) * (4 / i)
        j += 1
print(p)