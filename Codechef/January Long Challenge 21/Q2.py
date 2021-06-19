# https://www.codechef.com/JAN21C/problems/DECODEIT

T = int(input())
N = []
B = []

for t in range(T):
    N.append(int(input()))
    B.append(list(input()))

for t in range(T):
    n = N[t]
    b = B[t]
    b4 = []
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    for i in range(0,n,4):
        word = ''
        for j in range(i,i+4):
            word += b[j]
        b4.append(word)
    answer = ''
    for num in b4:
        answer += letters[int(num,2)]

    print(answer)
