# https://www.codechef.com/FEB21C/problems/MAXFUN

T = int(input())
N = []
A = []

for t in range(T):
    N.append(int(input()))
    A.append([int(x) for x in input().split()])

for t in range(T):
    n = N[t]
    a = A[t]
    a.sort()
    print(abs(a[0] - a[-1]) * 2)
