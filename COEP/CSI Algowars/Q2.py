T = int(input())
N = []
Q = []
A = []
Queries = []
for t in range(T):
    n, q = map(int, input().split())
    N.append(n)
    Q.append(q)
    A.append([int(x) for x in input().split()])
    queries = []
    for i in range(q):
        queries.append([int(x) for x in input().split()])
    Queries.append(queries)

for t in range(T):
    n = N[t]
    q = Q[t]
    a = A[t]
    queries = Queries[t]
    for i in range(q):
        query = queries[i]
        y = query[-1]
        x1 = min(query[:-1])
        x2 = max(query[:-1])
        if x1 > len(a):
            print(0)
        else:
            if x2 > len(a):
                x2 = len(a)
            u = 0
            d = 0
            s = 0
            for j in range(x1-1,x2):
                if a[j] > y:
                    if j == x1-1 or x2-1:
                        u += 1
                    else:
                        u += 2
                elif a[j] < y:
                    if j == x1 - 1 or x2 - 1:
                        d += 1
                    else:
                        d += 2
                else:
                    if j != x1-1 or j != x2-1:
                        s += 1
            if u == 1 and d == 1:
                print(1)
            else:
                print(min(u,d) + s)
