T = int(input())
Rows = []
for t in range(T):
    Rows.append(input())
for t in range(T):
    Row = Rows[t].split('0')
    counter = 0
    for i in Row:
        if i != '':
            counter += 1
    print(counter)