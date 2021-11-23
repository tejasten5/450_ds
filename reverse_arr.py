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
