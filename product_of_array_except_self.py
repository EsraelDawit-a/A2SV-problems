class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            r[i] = prefix
            prefix*=nums[i]

        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            r[j]*=postfix
            postfix*=nums[j]
        
        return r