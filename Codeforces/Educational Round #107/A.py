T = int(input())

for t in range(T):
    n = int(input())
    voters = [int(x) for x in input().split()]
    score = 0
    for voter in voters:
        if voter == 1 or voter == 3:
            score += 1
    print(score)