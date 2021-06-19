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
    letters = set()
    good_names = 0
    for i in range(n):
        si = s[i]
        letters.add(si[:1])
        if si[1:] not in s_dict:
            s_dict[si[1:]] = set()
        s_dict[si[1:]].add(si[:1])
    s_dict_l = list(s_dict.values())
    for i in range (len(s_dict)):
        S1 = s_dict_l[i]
        for j in range(i+1, len(s_dict)):
            S2 = s_dict_l[j]
            good_names += len(S1 - S2) * len(S2 - S1)
    print(good_names*2)