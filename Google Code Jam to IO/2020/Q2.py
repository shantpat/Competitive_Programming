# https://codingcompetitions.withgoogle.com/codejamio/round/000000000019ff03/00000000001b5e24

T = int(input())

for t in range(T):
    N = int(input())
    del_seq = [int(x) for x in input().split()]
    put_seq = ['0']*N
    graph = dict()

    for i in range(1, N+1, 2):
        graph[i] = [i+1]
        graph[i+1] = [i]

    for i in range(0, N, 2):
        graph[del_seq[i]].append(del_seq[i+1])
        graph[del_seq[i+1]].append(del_seq[i])
    pointer = 1
    for i in range(1, N+1):
        last = pointer
        if i % 2 == 0:
            put_seq[pointer-1] = 'L'
        else:
            put_seq[pointer-1] = 'R'

        if graph[pointer][0] == pointer:
            pointer = graph[pointer][1]
        else:
            pointer = graph[pointer][0]
        if i != N:
            graph[pointer].remove(last)
        print(graph)
    print(put_seq)