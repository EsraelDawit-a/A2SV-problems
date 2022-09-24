class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,len(nums)-1
        m = 0
        while l<r:
            m = max(m,(nums[l]+nums[r]))
            l+=1
            r-=1
        return m
            