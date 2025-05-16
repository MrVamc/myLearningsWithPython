def ascendingOrder(arr):
    size = len(arr)
    for i in range(size):
        temp = 0
        for j in range(i,size):
            if (arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

arr = [7,2,4,1,6,9,12]
print("Array before sorting: ")
print(arr)
print("Array after sorting: ")
ascendingOrder(arr)
print(arr)