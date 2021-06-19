# https://www.codechef.com/CODL2021/problems/CDS03

n, k = map(int, input().split())
Array = [int(x) for x in input().split()]
Answer = list(Array)
for i in range(k):
    print(Answer[i], end=' ')
for i in range (k,len(Answer),k):
    if k%2 ==0:
        print(Answer[i+k-1], end=' ')
    else:
        print(Answer[i], end=' ')