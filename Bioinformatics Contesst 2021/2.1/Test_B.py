T = int(input())
for t in range(T):
    s1 = input()
    s2 = input()
    for i in range(0,len(s1)-len(s2)):
        found = True
        for j in range(len(s2)):
            if s1[i+j] != s2[j]:
                found = False
        if found:
            print(i+1,end = ' ')
    print()