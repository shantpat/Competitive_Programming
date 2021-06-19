# https://www.codechef.com/DEC20B/problems/EVENPSUM
def no_of_eve(x):
    return int(x//2)


def no_of_odd(x):
    return int((x+1)//2)


T = int(input())
A = []
B = []
for t in range(T):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for t in range(T):
    a = A[t]
    b = B[t]
    print(no_of_eve(a)*no_of_eve(b) + no_of_odd(a)*no_of_odd(b))