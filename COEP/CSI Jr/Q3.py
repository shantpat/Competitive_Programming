MN = [int(x) for x in input().split()]
M = MN[0]
N = MN[1]
Matrix = []
row_min = []
row_max = []
col_min = []
col_max = []

for i in range(M):
    Matrix.append([int(x) for x in input().split()])
for i in range(1,61):
    rows = []

    for j in range(M):
        if i in Matrix[j]:
            rows.append(j)

    if rows:
        row_min.append(rows[0])
        row_max.append(rows[-1])
    else:
        row_min.append(-1)
        row_max.append(-1)

    cols = []

    for j in range(N):
        for k in range(M):
            if Matrix[k][j] == i:
                cols.append(j)

    if cols:
        col_min.append(cols[0])
        col_max.append(cols[-1])
    else:
        col_min.append(-1)
        col_max.append(-1)

Matrix_new = []
for i in range(M):
    r = []
    for j in range(N):
        r.append(0)
    Matrix_new.append(r)

for colour in range(1, 61):
    rmin = row_min[colour - 1]
    rmax = row_max[colour - 1]
    cmin = col_min[colour - 1]
    cmax = col_max[colour - 1]
    if rmin == -1:
        continue
    if cmin == -1:
        continue
    for i in range(rmin, rmax+1):
        for j in range(cmin, cmax+1):
            Matrix_new[i][j] = colour
    '''for row in Matrix_new:
        print(row)'''

'''for row in Matrix_new:
    print(row)
print('row_min', row_min)
print('row_max', row_max)
print('col_min', col_min)
print('col_max', col_max)'''

if Matrix_new == Matrix:
    print('true')
else:
    print('false')