T = int(input())

for t in range(T):
    l = [float(x) for x in input().split()]
    prod = 1
    for i in l:
        prod *= i
    if round(100/prod,ndigits=2) < 9.58:
        print('YES')
    else:
        print('NO')