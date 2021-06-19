T = int(input())

for t in range(T):
    n = int(input())
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    graph = dict()
    for i in range(n):
        graph[l1[i]] = l2[i]
    counter = 0
    visited = [0]*(n+1)

    for element in graph:
        if visited[element] == 0:
            first = element
            prev = first
            last = graph[element]
            while first != last:

                graph[prev] = 1
                prev = last
                last = graph[last]
                visited[prev] = 1
            counter += 1
    print(pow(2,counter,pow(10,9)+7))