class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        mx = 0
        
        # if we get 0 and k>0 pick it otherwise 
        # increment the left pointer 
        # and pick the currrent one
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if k == 0:
                    while nums[l]!=0:
                        l+=1
                    l+=1
                else:
                    k-=1
            mx =max(mx,i-l+1)
        return mx
       

       