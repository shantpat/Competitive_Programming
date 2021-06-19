# https://www.codechef.com/DEC20B/problems/VACCINE1

import math

d1, v1, d2, v2, p = map(int, input().split())
if d2 < d1:
    d = d1
    d1 = d2
    d2 = d
    v = v1
    v1 = v2
    v2 = v

print(int(d2 + math.ceil((p - (d2 - d1)*v1)/(v1 + v2)))-1)