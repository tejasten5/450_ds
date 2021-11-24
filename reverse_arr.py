# while loop
def reverse_arr(arr):
    start,end = 0,len(arr)-1
    
    while (start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr

result_arr = reverse_arr([50,49,48,47,46,45,44,43])
print(result_arr)

# for loop
def reverseArray(arr):
    j = len(arr)-1
    for i in range(len(arr)):
        if i < j:
            arr[i],arr[j-1] = arr[j-1],arr[i] 
        j -= 1
    print(arr)

arr = [65,64,63,62,61,60]
reverseArray(arr)
