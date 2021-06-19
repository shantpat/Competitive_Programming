N = int(input())
X = []
Y = []
Score = []

for n in range(N):
    x, y, s = map(int, input().split())
    X.append(x)
    Y.append(y)
    Score.append(s)
s_dict = dict()
for n1 in range(N):
    for n2 in range(n1+1,N):
        x1 = X[n1]
        x2 = X[n2]
        y1 = Y[n1]
        y2 = Y[n2]
        s1 = Score[n1]
        s2 = Score[n2]
        slope = None
        intercept = None
        if x1 - x2 == 0:
            slope = 'inf'
            intercept = 10**8+x1
        else:
            slope = (y1-y2)/(x1-x2)
            intercept = y1 - slope*x1
        if (slope, intercept) not in s_dict:
            s_dict[(slope, intercept)] = [n1, n2]
        else:
            s_dict[(slope, intercept)].append(n1)
            s_dict[(slope, intercept)].append(n2)

total_scores = [] + list(Score)
for ele in s_dict:
    Set = list(set(s_dict[ele]))
    score = 0
    for i in Set:
        score += Score[i]
    total_scores.append(score)
print(max(total_scores))
'''for ele in s_dict:
    print(ele)'''