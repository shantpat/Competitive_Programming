import itertools
T = int(input())
for i in range(T):
    a = list(input())
    req_nos = ''

    permutations = itertools.combinations_with_replacement('')