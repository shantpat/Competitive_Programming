T = int(input())
NKD = []
A = []

for t in range(T):
    NKD.append([int(x) for x in input().split()])
    A.append([int(x) for x in input().split()])

for t in range(T):
    n, k, d = map(int, NKD[t])
    a = A[t]
    problems = sum(a)
    contests = problems//k
    if contests > d:
        print(d)
    else:
        print(contests)

