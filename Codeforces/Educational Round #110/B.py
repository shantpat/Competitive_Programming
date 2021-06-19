def SieveOfEratosthenes(n):
    Prime_numbers = set()
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            Prime_numbers.add(p)
    return Prime_numbers


Prime_numbers = SieveOfEratosthenes(pow(10, 5)+1)

import math
T = int(input())

for t in range(T):
    n = int(input())
    numbers = [int(x) for x in input().split()]
    numbers.sort(reverse=True)
    counter = 0
    odd = []
    prime = []
    even = []
    for i in range(n):
        if numbers[i]%2 == 0:
            even.append(numbers[i])
        elif numbers[i] in Prime_numbers:
            prime.append(numbers[i])
        else:
            odd.append(numbers[i])
    even.sort()
    odd.sort()
    prime.sort()
    numbers = even + odd + prime
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(numbers[i], 2*numbers[j]) >1:
                counter += 1
    print(counter)




