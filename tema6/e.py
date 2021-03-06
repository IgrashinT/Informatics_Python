s = input()
a = s.find('f')
b = s.rfind('f')
if a == -1:
    pass
elif a == b:
    print(a)
else:
    print(a, b)