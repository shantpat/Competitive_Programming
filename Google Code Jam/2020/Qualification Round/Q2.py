T = int(input())
Strings = []

for t in range(T):
    X = [0] + list(input())
    X.append(0)
    Strings.append(X)

for t in range(T):
    String = Strings[t]
    String_diff = []
    for i in range(len(String)-1):
        String_diff.append(int(String[i+1]) - int(String[i]))
    answer = ''

    for i in range(len(String_diff)):
        if String_diff[i] >= 0:
            answer += '(' * String_diff[i]
        else:
            answer += ')' * abs(String_diff[i])
        answer += str(String[i+1])
    print('Case #'+str(t+1)+':',answer[:-1])


