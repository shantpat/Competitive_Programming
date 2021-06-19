Input_File = open('input.txt')
file_arr = []
for line in Input_File:
    A = [str(x) for x in line.split(',')]
    file_arr.append(A)

Employee_and_boss = []

for ele in file_arr:
    Employee_and_boss.append([ele[0].strip(),ele[2].strip()])


All_Top_Executives = []
for j in range(len(Employee_and_boss)-1,-1,-1):
    if Employee_and_boss[j][1] == 'NOBODY':
        All_Top_Executives.append(Employee_and_boss[j][0])
Dictionary = dict()
for ceo in All_Top_Executives:
    Employee_Array = [[ceo]]


    while True:
        current = Employee_Array[-1]
        ISfound = False
        for boss in Employee_Array[-1]:
            New = []
            for ele in Employee_and_boss:
                if ele[1] == boss:
                    ISfound = True
                    New.append(ele[0])
            if New != []:
                Employee_Array.append(New)
        if ISfound is False:
            break
    Dictionary[ceo] = Employee_Array[-1][-1]

Final_Answer = []
for ele in Dictionary:
    Final_Answer.append(ele+':'+" "+Dictionary[ele]+"\n")
Output_File = open('output.txt', 'w')
Output_File.writelines(Final_Answer)


