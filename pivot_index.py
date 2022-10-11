class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 2 : return 0
        
        pre = 0
        post = sum(nums)

        for i in range(len(nums)):
            # print(pre,post-nums[i])
            if pre == post-nums[i]: return i
            else:
                pre+=nums[i]
                post-=nums[i]
        return -1
            
