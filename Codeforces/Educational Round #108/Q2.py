T = int(input())


for i in range(T):
    N, M = map(int, input().split())
    graph = dict()
    lengths = dict()
    for j in range(M):
        u, v, w = map(int, input().split())
        graph[u] = v
        graph[v] = u
        lengths[(min(u, v), max(u, v))] = w

    hospitals = [int(x) for x in input().split()]
    for j in range(len(hospitals)):
        hospital = hospitals[i]
        distance = dict()
        



