# https://www.credit-suisse.com/pwp/hr/en/codingchallenge/#/questions/9

T = int(input())
N = []
Grids = []
answer = ''
for t in range(T):
    n = int(input())
    N.append(n)
    Grid = []
    for i in range(n):
        Grid.append([int(x) for x in input().split()])
    Grids.append(Grid)

for t in range(T):
    n = N[t]
    Grid = Grids[t]
    Sum_rows = []
    Sum_cols = []
    for i in range(n):
        row = Grid[i]
        Sum_rows.append(sum(row))
    for i in range(n):
        Sum = 0
        for j in range(n):
            Sum += Grid[j][i]
        Sum_cols.append(Sum)
    Sum_rows.sort()
    Sum_cols.sort()

    if Sum_rows == Sum_cols:
        answer += 'Possible'+','
    else:
        answer += 'Impossible' + ','

print(answer[:-1])
