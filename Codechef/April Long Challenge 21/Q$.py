T = int(input())

for t in range(T):
    x_original, y_original = map(int, input().split())
    path = ''
    x = abs(x_original)
    y = abs(y_original)
    if (abs(x) + abs(y)) % 2 == 0:
        print('Case #' + str(t + 1) + ':', 'IMPOSSIBLE')

    else:
        while x != 0 or y != 0:
            if x % 2 == 0:
                if (((y - 1) + (x))//2) % 2 != 0 or (x == 0 and y - 1 == 0):
                    y = (y - 1) // 2
                    x = (x) // 2
                    path += 'N'
                else:
                    y = (y + 1) // 2
                    x = (x) // 2
                    path += 'S'
            else:
                if(((y) + (x - 1))//2) % 2 != 0 or (x - 1 == 0 and y == 0):
                    y = (y) // 2
                    x = (x - 1) // 2
                    path += 'E'
                else:
                    y = (y) // 2
                    x = (x + 1) // 2
                    path += 'W'
            #print(x,y)
        answer = list(path)
        if y_original < 0:
            for i in range(len(path)):
                if path[i] == 'N':
                    answer[i] = 'S'
                elif path[i] == 'S':
                    answer[i] = 'N'

        if x_original < 0:
            for i in range(len(path)):
                if path[i] == 'E':
                    answer[i] = 'W'
                elif path[i] == 'W':
                    answer[i] = 'E'

        print('Case #' + str(t + 1) + ':', "".join(answer))


