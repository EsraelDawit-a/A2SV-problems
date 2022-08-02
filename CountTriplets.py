class Solution:
    def countTriplet(self, arr, n):
    # code here
        d={}
        for i in range(n):
            d[arr[i]]=i
        count=0
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i]+arr[j] in d:
                    count+=1 
                else:
                    continue
                
        return count