for i in range(100, 1000):
    x = i * i
    if str(x)[(len(str(x)) - 3):len(str(x))] == str(i):
        print(i)
