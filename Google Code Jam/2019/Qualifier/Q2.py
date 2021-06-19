# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

T = int(input())
N = []
Paths = []

for t in range(T):
    N.append(int(input()))
    Paths.append(input())

for t in range(T):
    n = N[t]
    path = Paths[t]
    answer = ''
    for i in range(len(path)):
        if path[i] == 'S':
            answer += 'E'
        else:
            answer += 'S'
    print('Case #' + str(t + 1) + ':', answer)
