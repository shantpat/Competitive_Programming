# https://codeforces.com/contests/1519

T = int(input())

for t in range(T):

    n = int(input())

    u = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]

    teams = dict()

    for i in range(n):
        if u[i] not in teams:
            teams[u[i]] = [s[i]]
        else:
            teams[u[i]].append(s[i])

    score = [0]*n
    for team in teams:
        skill = teams[team]
        skill.sort()
        c_skill = [0,skill[0]]

        for i in range(1,len(skill)):
            c_skill.append(skill[i] + c_skill[i])

        Sum = sum(skill)
        for i in range(len(skill)):
            score[i] += Sum - c_skill[len(skill)%(i+1)]
        '''print(team)
        print(skill)
        print(c_skill)
        print(Sum)
        print(score)
        print('------------')'''
    for i in score:
        print(str(i),end=' ')
    print()