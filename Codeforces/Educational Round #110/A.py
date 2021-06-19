T = int(input())
for t in range(T):
    s = [int(x) for x in input().split()]
    l1 = sorted([max(s[0],s[1]), max(s[2],s[3])])
    s.sort()
    l2 = sorted(s[2:])
    #print(l1,l2)
    if l1 == l2:
        print('YES')
    else:
        print('NO')