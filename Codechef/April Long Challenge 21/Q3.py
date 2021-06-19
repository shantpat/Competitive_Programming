T = int(input())

for t in range(T):
    N, K = map(int,input().split())
    String = list(input())
    score = 0
    for i in range(N):
        if String[i] != '*':
            String[i] = ' '
    
    joined_string = ''
    
    for i in String:
        joined_string += i
    
    if len(max(joined_string.split(' '))) >= K:
        print('YES')

    else:
        print('NO')
        