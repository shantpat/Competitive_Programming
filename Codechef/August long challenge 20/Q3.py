# Another Card Game Problem
# https://www.codechef.com/AUG20B/problems/CRDGAME3

T = int(input())
Pc = []
Pr = []

for t in range (T): # Input Format
    pc_pr = [int(x) for x in input().split()]
    Pc.append(pc_pr[0])
    Pr.append(pc_pr[1])

for t in range (T):
    pc = Pc[t]
    pr = Pr[t]

    if pc % 9 == 0:
        sc = int(pc//9)
    else:
        sc = int(pc//9) + 1

    if pr % 9 == 0:
        sr = int(pr//9)
    else:
        sr = int(pr//9) + 1

    if sr <= sc:
        print(1, sr)
    else:
        print(0, sc)

