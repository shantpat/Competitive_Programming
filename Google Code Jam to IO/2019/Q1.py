# https://codingcompetitions.withgoogle.com/codejamio/round/0000000000050fc5/0000000000054e9c

T = int(input())

for t in range(T):
    r, c, k = map(int, input().split())
    if r == 1 and c == 1 and k == 0:
        print('Case #'+str(t+1)+':', 'IMPOSSIBLE')
        continue
    elif r*c-k == 1:
        print('Case #'+str(t+1)+':', 'IMPOSSIBLE')
        continue
    else:
        matrix = []

        print('Case #'+str(t+1)+':', 'POSSIBLE')
        for i in range(r):
            matrix.append(['0']*c)

        if r == 1:
            matrix[0][0] = 'E'
            for i in range(1, c):
                matrix[0][i] = 'W'

        elif c == 1:
            matrix[0][0] = 'S'
            for i in range(1, r):
                matrix[i][0] = 'N'

        else:
            matrix[0][0] = 'E'
            for i in range(1,c):
                matrix[0][i] = 'W'

        for i in range(1,r):
            for j in range(c):
                matrix[i][j] = 'N'

        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if k == 0:
                    break
                matrix[i][j] = 'S'
                k -= 1

        for i in matrix:
            print("".join(i))
