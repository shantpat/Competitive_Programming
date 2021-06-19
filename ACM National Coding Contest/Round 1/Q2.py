Input_File = open('input.txt')
Array = []
for line in Input_File:
    Input = [str(x) for x in line.split(',')]
    Array.append(Input)

Dictionary = dict()
for c in Array:
    if c[2] in Dictionary:
        if Dictionary[c[2]] < int(c[1]):
            Dictionary[c[2]] = int(c[1])
    else:
        Dictionary[c[2]] = int(c[1])

Final_Answer = []
for Element in Dictionary:
    Final_Answer.append(str(Element)[1:]+" "+str(Dictionary[Element])+"\n")


Output_File = open('output.txt', 'w')
Output_File.writelines(Final_Answer)