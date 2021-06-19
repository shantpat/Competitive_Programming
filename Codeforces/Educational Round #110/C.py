T = int(input())

for t in range(T):
    s = list(input())
    stack = []
    se = []
    for i in range(len(s)):
        stack.append((s[i],i))
        #print(stack)
        if len(stack) > 1:
            if stack[0][0] == stack[-1][0] == '1' or stack[0][0] == stack[-1][0] == '0':
                if len(stack)%2 == 0:
                    se.append((stack[0][1], stack[-1][1]))
                    stack = []
            elif (stack[0][0] == '0' and stack[-1][0] == '1') or (stack[0][0] == '1' and stack[-1][0] == '0'):
                if len(stack) %2 != 0:
                    se.append((stack[0][1], stack[-1][1]))
                    stack = []
    print(se)