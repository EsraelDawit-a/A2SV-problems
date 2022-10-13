
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        # 1. compute prefix sum 
       
        for i in range(len(A)):
            if i > 0:
                A[i]+=A[i-1]
        A.insert(0,0)   # to make easy for competion

        # 2 then callculate L length Subarray sum Before M
        # we take sum of L number of items first then we take the rest sum of M items
        # |----L--- |---M---]
        # loop by L+M since it's the total length of Current window

        '''
        # nums = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
        prefix_sum = [0,0,6,11,13,15,20,21,30,34]

        If we want to calculate L subarray  before M means we take first L items 0 then 6,5

        

        if we Take L first [----L--- |---M---]
        we take the current sum and substract sum available before and after the window
        According to the algorithm is: Lsum =  prefixSum[i - M] - prefixSum[i - M - L] 

        N.B i starts from L+ M = 3
        # so for first itration i = 3
        
        Lsum = prefix_sum [3-2] - prefixSum[3-2-1] = pr[1]-pr[0] = 0-0 = 0
        now we get Lsum then we compute M after L items means sum of 6,5 wich is 11
        Msum = prefix_sum[i] - prefix_sum[i-M] = pre[3]-pr[3-2] = 11-0 = 11
        we will repeat this once in reverse order taking M first then L

        so the maximum sum we can get with current window is Lsum+Msum = 11+0 =11
        so we continue this until the end of array and taking maxmum sum available

        
        '''
        res = 0
        Lmax = 0
        Mmax = 0
        for l in range(L+M,len(A)):
            # Take L first
            Lsum = A[l-M] - A[l-M-L]
            Msum = A[l] - A[l-M]
            
            Lmax = max(Lmax,Lsum)
            res = max(res,Lmax+Msum)

            # 3 then callculate M length Subarray sum Before L
            # we take sum of M number of items first then we take the rest sum of L items
            # |----M--- |---L---]

            # Take M first
            Lsum = A[l] - A[l-L]
            Msum =  A[l-L] - A[l-L-M]  
            
            Mmax = max(Mmax,Msum)
            res = max(res,Mmax+Lsum)


        # 3 then callculate M length Subarray sum Before L
        # we take sum of M number of items first then we take the rest sum of L items
        # |----M--- |---L---]



        # for m  in range(L+M, len(A)):
        #     Lsum = A[m] - A[m-L]
        #     Msum =  A[m-L] - A[m-L-M]
            
        #     Mmax = max(Mmax,Msum)
        #     res = max(res,Mmax+Lsum)
        
        return res


                
