m, n = map(int, input().split())
Grid = []
for i in range(m):
    Grid.append(set(int(x) for x in input().split()))
s, e = map(int, input().split())

Queue = []

for Set in Grid:
    if s in Set:
        Queue.append([Set, 0])
        Grid.remove(Set)
isFound = False
for Set in Queue:
    if e in Set[0]:
        print(Set[1]+1)
        isFound = True
        break
    else:
        for List in Grid:
            if List.intersection(Set[0]) != set():
                Queue.append([List, Set[1]+1])
                Grid.remove(List)
if isFound is False:
    print(-1)