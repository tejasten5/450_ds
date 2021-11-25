
def rotate(arr, n):
    x = arr[n-1]
    for i in range(n-1,0,-1):
       arr[i] = arr[i-1]
       
    arr[0] = x
    
    
#     
# i = n-1
#     while(i > 0):
#         arr[i] = arr[i-1]
#         i -= 1
#     arr[0] = x
