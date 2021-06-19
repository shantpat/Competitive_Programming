T = int(input())

for t in range(T):
    n = int(input())
    histogram = [int(x) for x in input().split()]
    perimeter = histogram[0] + histogram[n-1]

    for i in range(1,n):
        perimeter += abs(histogram[i] - histogram[i-1])
        #print(abs(histogram[i] - histogram[i-1]))
    #print(perimeter)
    histogram_new = [0] + histogram + [0]

    for i in range(2,len(histogram_new)):
        if histogram_new[i-2] <= histogram_new[i-1] and histogram_new[i-1] >= histogram_new[i]:
            #print(abs(max(histogram_new[i - 2], histogram_new[i]) - histogram_new[i - 1]))
            perimeter -= abs(max(histogram_new[i-2], histogram_new[i]) - histogram_new[i-1])
            histogram_new[i-1] = max(histogram_new[i-2], histogram_new[i])

    print(perimeter)