# https://codeforces.com/contests/1519

T = int(input())

for t in range(T):
    a, b, d = map(int, input().split())
    if (d+1)*min(a,b) < max(a,b):
        print('NO')
    else:
        print('YES')