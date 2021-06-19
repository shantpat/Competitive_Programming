from collections import defaultdict


class Solution:

    def countCycle(self, n, pairs):
        self.graph = defaultdict(list)
        self.visited = defaultdict(lambda: 0)
        self.count = 0
        for var1, var2 in pairs:
            self.addEdge(var1, var2)

        for i in range(n):
            self.depthFirstSearch(i)

        return self.count

    def addEdge(self, var1, var2):
        self.graph[var1].append(var2)

    def depthFirstSearch(self, var):
        # if cycle is detected
        if self.visited[var] == -1:
            self.count += 1
            return
        # if depth first search has been completed on this variable
        if self.visited[var] == 1:
            return

        self.visited[var] = -1

        for neighb in self.graph[var]:
            self.depthFirstSearch(neighb)

        # mark depth first search on this variable as completed
        self.visited[var] = 1

T = int(input())
mod = pow(10,9)+7
for t in range(T):
    n = int(input())
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    pairs = []
    for i in range(n):
        pairs.append((l1[i], l2[i]))

    s = Solution()
    num = s.countCycle(n, pairs)
    print(pow(2,num,mod))
