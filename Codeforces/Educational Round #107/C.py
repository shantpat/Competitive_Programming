n, q = map(int, input().split())
cards = [int(x) for x in input().split()]
queries = [int(x) for x in input().split()]
colors = dict()
for i in range(n):
    if cards[i] not in colors:
        colors[cards[i]] = i

for q in queries:
    print(colors[q] + 1, end=' ')
    for color in colors:
        if colors[color] < colors[q]:
            colors[color] += 1
    colors[q] = 0

