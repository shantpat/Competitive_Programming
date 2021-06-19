# https://www.codechef.com/JAN21C/problems/FAIRELCT

T = int(input())
N = []
M = []
Ai = []
Bi = []

for t in range(T):
    n, m = map(int, input().split())
    N.append(n)
    M.append(m)
    Ai.append([int(x) for x in input().split()])
    Bi.append([int(x) for x in input().split()])

for t in range(T):
    n = N[t]
    m = M[t]
    ai = Ai[t]
    bi = Bi[t]
    ai.sort()
    bi.sort(reverse=True)
    di = []
    for i in range(min(m,n)):
        di.append(bi[i]-ai[i])
    diff = (sum(bi) - sum(ai))//2
    counter = 0
    if diff < 0:
        print(0)
    else:
        for i in range(len(di)):
            if di[i] < 0:
                break
            diff -= di[i]
            counter += 1
            if diff < 0:
                break
        if diff >= 0:
            print(-1)
        else:
            print(counter)