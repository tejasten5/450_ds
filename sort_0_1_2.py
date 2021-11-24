# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

class Solution:
    def sort012(self,arr,n):
        # code here
        i,j,min_ele = 0,0,0        
        c0,c1,c2 = 0,0,0
        
        while j < len(arr):
            if (arr[j] == 0 ):
                c0 += 1
            elif (arr[j] == 1):
                c1 += 1
            elif (arr[j] == 2):
                c2 += 1
            j += 1
            
        while c0 > 0:
            arr[i] = 0
            i += 1
            c0 -= 1
            
        while c1 > 0:
            arr[i] = 1
            i += 1
            c1 -= 1
            
        while c2 > 0:
            arr[i] = 2
            i += 1
            c2 -= 1
        return arr
