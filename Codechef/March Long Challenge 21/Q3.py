T = int(input())

for t in range(T):
    R, C = map(int, input().split)
    Matrix = []
    for r in range(R):
        Matrix.append([int(x) for x in input().split()])
    for i in range R*C