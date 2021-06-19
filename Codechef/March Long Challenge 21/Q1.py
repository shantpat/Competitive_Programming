T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    Matrix = []
    Score_Matrix = []

    for r in range(R):
        row = []
        for c in range(C):
            row.append([0,0,0,0]) # up down left right
        Score_Matrix.append(row)

    for r in range(R):
        Matrix.append([int(x) for x in input().split()])

    for r in range(R):
        Row = Matrix[r]
        index = 0
        while index < C:
            s = None
            e = None
            if Row[index] == 1:
                s = index
                score = 0
                while index < C:
                    if Row[index] == 1:
                        score += 1
                        index += 1
                    else:
                        break
                for i in range(s,s+score):
                    Score_Matrix[r][i][2] = i-s +1
                    Score_Matrix[r][i][3] = score - (i-s)
            else:
                index += 1

    for ele in range(C):
        column = [val[ele] for val in Matrix]
        index = 0
        while index < R:
            s = None
            if column[index] == 1:
                s = index
                score = 0
                while index < R:
                    if column[index] == 1:
                        score += 1
                        index += 1
                    else:
                        break
                for i in range(s,s+score):
                    Score_Matrix[i][ele][0] = i-s +1
                    Score_Matrix[i][ele][1] = score - (i-s)
            else:
                index += 1
    '''for r in Score_Matrix:
        print(r)'''
    score = 0
    for r in range(R):
        for c in range(C):
            choices = [[0,2],[0,3],[1,2],[1,3]]
            element = Score_Matrix[r][c]
            for choice in choices:
                c1,c2 = map(int,choice)
                if element[c1] >=2 and element[c2] >= 2:
                    score += (min(element[c1]-1, (element[c2]//2)-1) + min(element[c2]-1, (element[c1]//2)-1))
    print('Case #'+str(t+1)+':',score)

