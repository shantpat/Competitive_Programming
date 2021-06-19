T = int(input())
S = []
E = []
N = []

for t in range(T):
    n = int(input())
    N.append(n)
    s1 = []
    e1 = []
    for i in range(n):
        s, e = map(int, input().split())
        s1.append([s, 's', i])
        e1.append([e, 'e', i])
    S.append(s1)
    E.append(e1)

for t in range(T):
    n = N[t]
    s = S[t]
    e = E[t]
    Time = s+e
    Time.sort()

    is_J_free = True
    is_C_free = True
    is_impossible = False
    J = dict()
    C = dict()
    answer = [0]*n

    for i in range(2*n):
        element = Time[i]
        if element[1] == 's':
            if is_J_free:
                J[element[2]] = 1
                is_J_free = False
            elif is_C_free:
                C[element[2]] = 1
                is_C_free = False
            else:
                is_impossible = True
                break

        elif element[1] == 'e':
            if element[2] in J:
                del J[element[2]]
                answer[element[2]] = 'J'
                is_J_free = True
            elif element[2] in C:
                del C[element[2]]
                answer[element[2]] = 'C'
                is_C_free = True
            else:
                print('Error')
    Answer = ''
    for a in answer:
        Answer += str(a)
    if is_impossible:
        print('Case #'+str(t+1)+':', 'IMPOSSIBLE')
    else:
        print('Case #'+str(t+1)+':', Answer)



