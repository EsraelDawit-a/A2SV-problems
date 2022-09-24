class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
	
        nums.sort()
        j = 0
        ans = 1
        for i in range(1,len(nums)):
            reqd = nums[i] - nums[i-1]
            length = (i - j) * reqd
            k -= length
            while k < 0:
                k += nums[i] - nums[j]
                j += 1
            ans = max(ans,i-j+1)
        return ans