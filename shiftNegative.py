
def shiftNegative(arr):
    j = 0
    for i in range(len(arr)):
        if (arr[i] < 0):
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    print(arr)
    
arr = [-3,-1, 2,  4, 5, 6, -7, 8, 9]
shiftNegative(arr)
