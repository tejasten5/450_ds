def findElement(arr):
    min_ele,max_ele = arr[0],0
    i = 0
    while(i < len(arr)  ):
        
        if arr[i] > max_ele:
            max_ele = arr[i]
        if arr[i] < min_ele:
            min_ele = arr[i]
        i += 1
    print(max_ele,min_ele)

arr = [45,47,89,45,256,21,10,45,10,8,488,2564,15,12358,48,69]

try:
    findElement(arr)
except Exception as e:
    print(e)
