# https://codeforces.com/contests/1519

n = int(input())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

matrix = []
for i in range(n):
    matrix.append([0]*n)
max_score = 0
for d in range(1,n):
    for i in range(n-d):
        score = (a[i+d]*b[i] + a[i]*b[i+d]) - (a[i]*b[i] + a[i+d]*b[i+d]) + matrix[i+1][i+d-1]
        matrix[i][i+d] = score
        max_score = max(score,max_score)

def_score = 0
for i in range(n):
    def_score += a[i]*b[i]
print(def_score+max_score)


