# https://www.codechef.com/JAN21C/problems/WIPL

T = int(input())
NK = []
Hi = []

for t in range(T):
    NK.append(input().split())
    Hi.append([int(x) for x in input().split()])

for t in range(T):
    n, k = map(int, NK[t])
    hi = Hi[t]
    hi.sort(reverse = True)
    t1 = 0
    t2 = 0
    counter = 0
    s1 = False
    s2 = False
    for i in range(0, n, 2):
        t1 += hi[i]
        hi[i] = 0
        counter +=1
        if t1 >= k:
            s1 = True
            break
    for i in range(n):
        t2 += hi[i]
        if hi[i] != 0:
            counter += 1
        hi[i] = 0
        if t2 >= k:
            s2 = True
            break
    if s1 and s2:
        print(counter)
    else:
        print(-1)