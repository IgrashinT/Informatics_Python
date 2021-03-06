def WhatColour(x, y):
    if x % 2 == 0:
        if y % 2 == 0:
            return 1
        else: return 0
    else:
        if y % 2 == 0:
            return 0
        else: return 1
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if WhatColour(a, b) == WhatColour(c, d): print("YES")
else: print("NO")