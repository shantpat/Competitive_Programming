T = int(input())
N = []
Matrix = []
for t in range(T):
    n = int(input())
    N.append(n)
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input().split()])
    Matrix.append(matrix)

row_counter = 0
col_counter = 0

for t in range(T):
    n = N[t]
    matrix = Matrix[t]

    for r in range(n):
        rd = dict()
        for c in range(n):
            element = matrix[r][c]
            if element not in rd:
                rd[element] = 1
            else:
                row_counter += 1
                break

    for c in range(n):
        cd = dict()
        for r in range(n):
            element = matrix[r][c]
            if element not in cd:
                cd[element] = 1
            else:
                col_counter += 1
                break

    trace = 0
    for i in range(n):
        trace += matrix[i][i]

    print('Case #'+str(t+1)+':', trace, row_counter, col_counter)

