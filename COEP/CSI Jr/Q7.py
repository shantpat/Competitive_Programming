
m, n = map(int, input().split())
Grid = []
for i in range(m):
    Grid.append([int(x) for x in input().split()])
s, e = map(int, input().split())

Links = []
for i in range(m-1):
    Links.append(0)
for i in range(n):
    for j in range(m-1):
        if Grid[j][i] == Grid[j+1][i]:
            Links[j] = 1
if m == 1:
    print(1)
else:
    s_coordinates = None
    e_coordinates = None
    for i in range(m):
        for j in range(n):
            if Grid[i][j] == s:
                s_coordinates = i
            elif Grid[i][j] == e:
                e_coordinates = i

    if s_coordinates == e_coordinates:
        print(1)
    elif s_coordinates < e_coordinates:
        isPossible = True
        for i in range(s_coordinates, e_coordinates):
            if Links[i] == 0:
                isPossible = False
        if isPossible:
            print(abs(e_coordinates - s_coordinates) + 1)
        else:
            print(-1)
    else:
        isPossible = True
        for i in range(e_coordinates, s_coordinates):
            if Links[i] == 0:
                isPossible = False
        if isPossible:
            print(abs(s_coordinates - e_coordinates) + 1)
        else:
            print(-1)


