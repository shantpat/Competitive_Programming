# https://www.codechef.com/JAN21C/problems/BILLRD

T = int(input())
NKXY = []

for t in range(T):
    NKXY.append([int(x) for x in input().split()])

for t in range(T):
    n, k, x, y = map(int, NKXY[t])
    if x == y:
        print(n, n)
    elif x > y:
        x = n - x
        Points = [(n - x - y, 0), (n, x + y), (x + y, n), (0, n - x - y)]
        print(Points[k % 4][0], Points[k % 4][1])
    else:
        y = n - y
        Points = [(0, n - x - y), (x + y, n), (n, x + y), (n - x - y, 0)]
        print(Points[k % 4][0], Points[k % 4][1])

