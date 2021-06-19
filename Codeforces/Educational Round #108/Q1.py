N = int(input())
bags = [float(x) for x in input().split()]
bags.sort()
bag_dict = dict()
ptr_s = 0
ptr_e = len(bags) - 1
score = 0
while ptr_s < ptr_e:

    if bags[ptr_s] + bags[ptr_e] <= 3:
        ptr_s += 1
        ptr_e -= 1
        score += 1
        continue
    ptr_e -= 1

print(N-2*score + score)
