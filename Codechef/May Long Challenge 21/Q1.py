# https://www.codechef.com/MAY21C/problems/SOLBLTY

T = int(input())

for t in range(T):
    X, A, B = map(int,input().split())
    print((A + (100 -X)*B)*10)