# https://www.codechef.com/FEB21C/problems/HDIVISR

n = int(input())
for i in range(10,0,-1):
    if n % i == 0:
        print(i)
        break
