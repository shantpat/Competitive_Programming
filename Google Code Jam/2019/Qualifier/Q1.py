#

T = int(input())
N = []

for t in range(T):
    N.append(input())

for t in range(T):
    n = list(N[t])
    num1 = ''
    num2 = ''
    for i in range(len(n)):
        if n[i] == '4':
            num1 += '2'
            num2 += '2'
        else:
            num1 += n[i]
            num2 += '0'

    print('Case #' + str(t + 1) + ':', int(num1), int(num2))