# Chef Wars - Return of the Jedi
# https://www.codechef.com/AUG20B/problems/CHEFWARS

T = int(input())
H = []
P = []

for t in range(T): # Input Format
    h_p = [int(x) for x in input().split()]
    H.append(h_p[0])
    P.append(h_p[1])

for t in range(T):
    h = H[t]
    p = P[t]

    if h > 2*p:
        print(0)

    else:
        print(1)