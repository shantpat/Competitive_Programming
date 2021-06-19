# Smallest KMP
# https://www.codechef.com/AUG20B/problems/SKMP

n = int(input())
S = []
P = []

for i in range (n):
    S.append(list(input()))
    P.append(list(input()))

for i in range (n):
    s = S[i]
    p = P[i]
    ds = [0]*26
    dp = [0]*26
    df = [0]*26
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for j in s:
        ds[letters.index(j)] += 1
    for j in p:
        dp[letters.index(j)] += 1

    for j in range(26):
        df[j] = ds[j] - dp[j]

    is_before = False
    counter = 1
    first = p[0]

    while True:
        if counter == len(p):
            break
        if p[counter] < first:
            is_before = False
            break
        elif p[counter] > first:
            is_before = True
            break
        counter += 1

    string = ''
    I = letters.index(first)
    p_str = "".join(p)
    for nl in range(I):
        string += letters[nl]*df[nl]

    if is_before:
        string += letters[I]*df[I]
        string += p_str
    else:
        string += p_str
        string += letters[I] * df[I]

    for nl in range (I+1,26):
        string += letters[nl] * df[nl]

    print(string)











