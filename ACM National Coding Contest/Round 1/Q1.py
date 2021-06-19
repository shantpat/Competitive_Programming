# Q1
file = open('input.txt')

Array = []
for line in file:
    Input = [str(x) for x in line.split(',')]
    Array.append(Input)

Final_Answer = []
for case in Array:
    Final_Answer.append(int(case[1]))
f_answer = str(min(Final_Answer))
file = open('output.txt', 'w')
file.write(str(f_answer))