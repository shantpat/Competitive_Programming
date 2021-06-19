mn = [int(x) for x in input().split()]
m = mn[0]
n = mn[1]
Matrix = []

for i in range(m):
    Matrix.append([int(x) for x in input().split()])
ones = 0
for i in range(m):
    ones += Matrix[i].count(1)

kaivalyas = 0

for i in range(m):
    if Matrix[i].count(1) == 1:
        ind = Matrix[i].index(1)
        col_ones = 0
        for j in range(m):
            if Matrix[j][ind] == 1:
                col_ones += 1
        if col_ones == 1:
            kaivalyas += 1
print(ones - kaivalyas)
