class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        m = float('inf')
        i,j = 0,0
        while j<=len(nums) and i<=len(nums):
            if s >= target:
                m = min(m,j-i)
                s-=nums[i]
                i+=1
            else:
                if j<len(nums) :s+=nums[j]
                j+=1
                
        return m if m!=float("inf") else 0
