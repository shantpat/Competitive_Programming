T = int(input())


def check_ev(grid):
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(grid[i])):
            if i%2 == 0 and j%2 == 0 and row[j] == 'R':
                return False, None
            elif i%2 == 0 and j%2 != 0 and row[j] == 'W':
                return False, None
            elif i%2 != 0 and j%2 == 0 and row[j] == 'W':
                return False, None
            elif i%2 != 0 and j%2 != 0 and row[j] == 'R':
                return False, None
    return True, 'ev'


def check_od(grid):
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(grid[i])):
            if i%2 == 0 and j%2 == 0 and row[j] == 'W':
                return False, None
            elif i%2 == 0 and j%2 != 0 and row[j] == 'R':
                return False, None
            elif i%2 != 0 and j%2 == 0 and row[j] == 'R':
                return False, None
            elif i%2 != 0 and j%2 != 0 and row[j] == 'W':
                return False, None
    return True, 'od'


for t in range(T):
    n, m = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    e1,e2 = check_ev(grid)
    o1,o2 = check_od(grid)
    #print(e1,o1)
    if e1 == False and o1 == False:
        print('NO')
    elif o1:
        print('YES')
        for i in range(n):
            for j in range(m):
                if i%2 == 0 and j%2 == 0:
                    print('R',end='')
                elif i % 2 != 0 and j % 2 != 0:
                    print('R', end='')
                else:
                    print('W',end='')
            print()
    else:
        print('YES')
        for i in range(n):
            for j in range(m):
                if i%2 == 0 and j%2 == 0:
                    print('W',end='')
                elif i % 2 != 0 and j % 2 != 0:
                    print('W', end='')
                else:
                    print('R',end='')
            print()

