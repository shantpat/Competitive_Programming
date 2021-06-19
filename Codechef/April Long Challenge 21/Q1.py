Socks = [int(x) for x in input().split()]
d = dict()
for i in Socks:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

found = False

for i in d:
    if d[i] >= 2:
        found = True
        break

if found:
    print('YES')
else:
    print('NO')