# https://www.codechef.com/DEC20B/problems/POSPREFS

T = int(input())
N = []
K = []

for t in range(T):
    n, k = map (int, input().split())
    N.append(n)
    K.append(k)

for t in range(T):
    n = N[t]
    k = K[t]
    if k >= (n+1)//2:
        x = 2*(n-k)
        answer = ''
        for i in range(n):
            if i < x:
                if i % 2 == 0:
                    answer += str(i+1) + ' '
                else:
                    answer += str(-i-1) + ' '
            else:
                answer += str(i+1) + ' '
        print(answer)
    else:
        counter = k
        answer = ''
        for i in range(n):
            if counter != 0:
                if i % 2 == 0:
                    answer += str(i+1) + ' '
                    counter -= 1
                else:
                    answer += str(-i-1) + ' '

            else:
                answer += str(-i-1) + ' '
        print(answer)
