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
    s_dict = dict()
    s_parts = []

    for i in range(n):
        si = s[i]
        if si[1:] not in s_dict:
            s_dict[si[1:]] = set()
        s_dict[si[1:]].add(si[:1])
    print(s_dict)

    for i in range(n):
        si = s[i]
        s_parts.append((si, si[:1], si[1:]))
    print(s_parts)

    good_name = 0
    for w1 in range(n):
        W1 = s_parts[w1]
        for w2 in range(w1 + 1, n):
            W2 = s_parts[w2]
            if W2[1] not in s_dict[W1[2]] and W1[1] not in s_dict[W2[2]]:
                good_name += 2
    print(good_name)