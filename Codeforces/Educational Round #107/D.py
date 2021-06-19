n, k = map(int, input().split())
eulerian_cycle = ''
letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

for i in range(1,k+1):
    eulerian_cycle += letters[i-1]*2
for i in range(1,k):
    current_var = k-i
    eulerian_cycle += str(letters[current_var-1])
    for j in range(1,i):
        eulerian_cycle += str(letters[current_var+j])
        eulerian_cycle += str(letters[current_var-1])
eulerian_cycle = eulerian_cycle[:-1]

print(eulerian_cycle*(n//(k**2)) + eulerian_cycle[:(n%(k**2))])



