string = list(input())
l = len(string)
counter = 0
increasing = None
for i in range(0, l-1):
    if increasing == None:
        if string[i] < string[i+1]:
            increasing = True
        elif string[i] == string[i+1]:
            pass
        else:
            increasing = False
    elif increasing:
        if string[i] > string[i+1]:
            counter += 1
            increasing = None
    else:
        if string[i] < string[i+1]:
            counter += 1
            increasing = None
print(counter + 1)