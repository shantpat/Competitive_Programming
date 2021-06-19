T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    grid = []
    found_sequence = dict()
    counter = 1
    answer = []
    for i in range(n):
        grid.append(list(input()))
    for i in range(m):
        sequence = ''
        for j in range(n):
            sequence += grid[j][i]
        if sequence not in found_sequence:
            answer.append(counter)
            found_sequence[sequence] = counter
            counter += 1

        else:
            answer.append(found_sequence[sequence])
    print(len(found_sequence))
    for i in answer:
        print(i, end=' ')
    print()