# https://www.codechef.com/FEB21C/problems/FROGS
import math

T = int(input())
N = []
W = []
L = []

for t in range(T):
    N.append(int(input()))
    W.append([int(x) for x in input().split()])
    L.append([int(x) for x in input().split()])

for t in range(T):
    n = N[t]
    w = W[t]
    l = L[t]
    wl = []

    for i in range(n):
        wl.append((w[i], l[i], i))

    wl.sort()
    taps = 0
    current_l = -1

    for i in range(n):
        w1 = wl[i][0]
        l1 = wl[i][1]
        p1 = wl[i][2]
        if current_l == -1:
            current_l = p1
        elif p1 == current_l:
            taps += 1
            current_l += l1
        elif p1 < current_l:
            j = math.ceil((current_l - p1)/l1)
            if current_l == j*l1 + p1:
                j += 1
            taps += j
            current_l = p1 + j*l1
        else:
            current_l = p1

    print(taps)
