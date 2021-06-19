T = int(input())
score_list = [6,11,15,18,20,21]
inc_stack = {0: '000000', 1: '000010', 2: '000200', 3:'001200'}
scd_stack = {0: '004000', 1: '013000', 2: '022000', 3:'031000', 4: '040000'}
mid_score = 44
for t in range(T):
    n = int(input())
    score = 0
    inc_stack_val = n % 4
    scd_stack_val = 0
    mid_stack_val = 0
    if n//4 >= 1:
        scd_stack_val = 1
        mid_stack_val = n//4-1
    for i in range(len(inc_stack[inc_stack_val])):
        score += int(inc_stack[inc_stack_val][i])*score_list[i]
    if scd_stack_val == 1:
        for i in range(len(scd_stack[inc_stack_val])):
            score += int(scd_stack[inc_stack_val][i])*score_list[i]
    score += mid_score*mid_stack_val
    print(score)