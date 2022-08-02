class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if set(nums) == nums:
            return 0
        else:
            c = 0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] == nums[j]:
                        c+=1
            return c