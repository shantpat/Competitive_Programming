Input_File = open('input.txt')
Array = []
for line in Input_File:

    Input = [str(x) for x in line.split(',')]

    Array.append(Input)

Employee_and_Boss = []

for element in Array:

    Employee_and_Boss.append([element[0].strip(), element[2].strip()])

Last_CEO = None

for j in range(len(Employee_and_Boss)-1,-1,-1):

    if Employee_and_Boss[j][1] == 'NOBODY':

        Last_CEO = Employee_and_Boss[j][0]

        break

Employee_Array = [[Last_CEO]]

'''while True:

    isFound = False

    for boss in Employee_Array[-1]:

        Latest = []

        for ele in Employee_and_Boss:

            if ele[1] == boss:

                found = True

                Latest.append(ele[0])

        if Latest != []:

            Employee_Array.append(Latest)

    if isFound is False:

        break'''

while True:

    ISfound = False

    for boss in Employee_Array[-1]:

        Latest = []

        for ele in Employee_and_Boss:

            if ele[1] == boss:

                ISfound = True

                Latest.append(ele[0])

        if Latest != []:

            Employee_Array.append(Latest)

    if ISfound is False:

        break


Output_File = open('output.txt', 'w')
Output_File.write(Employee_Array[-1][-1])


