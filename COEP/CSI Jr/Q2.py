n = int(input())
List = [int(x) for x in input().split()]
List_e = []
for i in range(n):
    List_e.append((List[i], i))
counter = 1
List_e.sort()
List_r = [(List_e[0][1], 1)]
for i in range(1, len(List)):
    if List_e[i - 1][0] == List_e[i][0]:
        List_r.append((List_e[i][1], counter))
    else:
        counter += 1
        List_r.append((List_e[i][1], counter))
List_r.sort()

answer = ''
for i in range(n):
    answer += str(List_r[i][1])+' '
print(answer)