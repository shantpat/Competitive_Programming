import heapq as hq

class Node:
    def __init__(self, value):

        self.value = value
        self.edges = set()

        self.distance = -1
        self.visited = False

    @staticmethod
    def add_edge(a, b, dist):
        a.edges.add((b, dist))
        b.edges.add((a, dist))


def calc_distance(start):

    h = []

    start.distance = 0

    hq.heappush(h, (start.distance, start))

    while len(h) > 0:

        cur = hq.heappop(h)

        # check if the nodes has been updated
        if cur[0] != cur[1].distance:
            continue

        for e in cur[1].edges:
            new_distance = cur[1].distance + e[1]

            if e[0].distance < 0 or new_distance < e[0].distance:
                e[0].distance = new_distance
                hq.heappush(h, (new_distance, e[0]))


def create_graph1(n,paths):
    Nodes = []
    for i in range(n):
        Nodes.append(Node(i+1))


    for path in paths:
        Node.add_edge(Nodes[path[0]-1], Nodes[path[1]-1], path[2])


    return Nodes


def print_nodes(nodes,dic):

    #print('print nodes --')
    for node in nodes:
        #print(f'value: {node.value}, distance: {node.distance}')
        dic[node.value] = min(node.distance,dic[node.value])
    return dic


T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    paths = []

    for j in range(M):
        u, v, w = map(int, input().split())
        paths.append([u,v,w])
    h = int(input())
    hospitals = [int(x) for x in input().split()]
    nodes = create_graph1(N,paths)
    dic = dict()
    for j in range(N):
        dic[j+1] = 10**9

    for hospital in hospitals:
        calc_distance(nodes[hospital-1])
        dic = print_nodes(nodes,dic)

    for node in nodes:
        print(node.distance,end = ' ')
    print()





