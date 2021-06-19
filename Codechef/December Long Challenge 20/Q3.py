# https://www.codechef.com/DEC20B/problems/VACCINE2
import math
T = int(input())
N = []
D = []
Ages = []

for t in range(T):
    n, d = map(int, input().split())
    N.append(n)
    D.append(d)
    Ages.append([int(x) for x in input().split()])

for t in range(T):
    n = N[t]
    d = D[t]
    ages = Ages[t]
    risk = 0
    for i in ages:
        if i >= 80 or i <= 9:
            risk += 1

    print(math.ceil(risk/d) + math.ceil((n-risk)/d))
