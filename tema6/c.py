import math as mt
s = input()
print(s[mt.ceil((len(s) / 2)):], end = '')
print(s[:mt.ceil(len(s) / 2)])