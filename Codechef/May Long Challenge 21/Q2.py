# https://www.codechef.com/MAY21C/problems/LKDNGOLF

T = int(input())

for t in range(T):
    n, x, k = map(int,input().split())
    if x % k == 0:
        print('YES')
    elif x+(n)