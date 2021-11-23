def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        
        return arr[k-1]
        
  arr = [11,25,3,25,4,98]
  kthSmallest(arr,0,5)
