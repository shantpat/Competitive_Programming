# https://www.codechef.com/FEB21C/problems/TEAMNAME

T = int(input())
N = []
S = []

for t in range(T):
    N.append(int(input()))
    S.append(input().split())

for t in range(T):
    n = N[t]
    s = S[t]
    set_s = set(s)
    good_name = 0
    for w1 in range(n):
        W1 = s[w1]
        for w2 in range(w1+1, n):
            W2 = s[w2]
            N1 = W1[:1] + W2[1:]
            N2 = W2[:1] + W1[1:]
            if N1 not in set_s and N2 not in set_s:
                good_name += 2
    print(good_name)