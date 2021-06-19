# Chef and Linear Chess
# https://www.codechef.com/AUG20B/problems/LINCHESS

T = int(input())
N = []
K = []
P = []

for t in range (T):
    n_k = [int(x) for x in input().split()]
    N.append(n_k[0])
    K.append(n_k[1])
    P.append([int(x) for x in input().split()])

for t in range (T):
    moves = []
    n = N[t]
    k = K[t]
    p = P[t]

    for i in range (n):
        if abs(p[i] - k) % p[i] == 0:
            moves.append(int(abs(p[i] - k) / p[i]))
        else:
            moves.append(10**10)

    if len(set(moves)) == 1:
        print(-1)
    else:
        Min = min(moves)
        I = moves.index(Min)
        print(p[I])

