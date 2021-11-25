
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        max_ele = 0
        for i in range(n):
            
            if arr[i] > max_ele:
                max_ele = arr[i]
                idx = i
            
               
        return idx
