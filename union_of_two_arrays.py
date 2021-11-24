class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        # c = a + b
        # context = {}
        # for i in c:
        #     if i in context:
        #         context[i] += 1
        #     else:
        #         context[i] = 1
        return len(set(a + b))
