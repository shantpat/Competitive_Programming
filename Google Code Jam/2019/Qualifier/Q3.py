import math

def primeFactors(n):
    pfactors = []
    while n % 2 == 0:
        pfactors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            pfactors.append(int(i))
            n = n // i

    if n > 2:
        pfactors.append(int(n))

    return pfactors


T = int(input())
N = []
L = []
Ciphertext = []

for t in range(T):
    n, l = map(int, input().split())
    N.append(n)
    L.append(l)
    Ciphertext.append([int(x) for x in input().split()])

for t in range(T):
    n = N[t]
    l = L[t]
    ciphertext = Ciphertext[t]
    prime_set = set()
    prime_list = []

    for i in range(l):
        c = ciphertext[i]
        if i == 0:
            pf = primeFactors(c)
            prime_list.append(pf)
            prime_set.add(int(pf[0]))
            prime_set.add(int(pf[1]))

        else:
            num1 = prime_list[-1][0]
            num2 = prime_list[-1][1]
            if c % num1 == 0:
                prime_list.append([num1, c//num1])
                prime_set.add(c//num1)
            elif c % num2 == 0:
                prime_list.append([num2, c//num2])
                prime_set.add(c // num2)
            else:

    prime_set_list = list(prime_set)
    prime_set_list.sort()
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_dict = dict()

    for j in range(len(letters)):
        letters_dict[prime_set_list[j]] = letters[j]

    n2 = prime_list[1][0]
    n1 = 0
    for ele in prime_list[0]:
        if ele != n2:
            n1 = ele

    prime_list[0] = [n1, n2]

    answer = ''
    for j in range(l):
        answer += letters_dict[prime_list[j][0]]
        if j == l-1:
            answer += letters_dict[prime_list[j][1]]
    print('Case #' + str(t + 1) + ':', answer)