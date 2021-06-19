l = 101
grid = []
for i in range(l):
    row = []
    for j in range(l):
        row.append(set())
    grid.append(row)
grid[0][0].add(0)
for x in range(l):
    for y in range(l):

        if y > 0:
            for element in grid[x][y-1]:
                grid[x][y].add(element+x+1)

        if x > 0:
            for element in grid[x-1][y]:
                grid[x][y].add(element+y+1)

T = int(input())
for t in range(T):
    x, y, k = map(int, input().split())
    if k in grid[x-1][y-1]:
        print('YES')
    else:
        print('NO')

