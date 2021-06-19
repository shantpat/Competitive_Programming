# https://www.codechef.com/FEB21C/problems/MEET

T = int(input())
P = []
N = []
L = []
R = []

for t in range(T):
    P.append(input())
    N.append(int(input()))
    l1 = []
    r1 = []
    for n in range(N[-1]):
        lr = input()
        l = lr[:8]
        r = lr[9:]
        l1.append(l)
        r1.append(r)
    L.append(l1)
    R.append(r1)


def convert_to_minutes(time):
    if time == '12:00 AM':
        minutes = 0
    elif time == '12:00 PM':
        minutes = 12*60
    else:
        t, ap = time.split(' ')
        h, m = t.split(':')
        minutes = int(h)*60 + int(m)
        if ap == 'AM' and h == '12':
            minutes -= 12*60
        if ap == 'PM' and h != '12':
            minutes += 12*60
    return minutes


for t in range(T):
    p = P[t]
    n = N[t]
    l = L[t]
    r = R[t]

    answer = ''
    p = convert_to_minutes(p)
    for i in range(n):
        lm = convert_to_minutes(l[i])
        rm = convert_to_minutes(r[i])
        if lm <= p <= rm:
            answer += '1'
        else:
            answer += '0'
    print(answer)