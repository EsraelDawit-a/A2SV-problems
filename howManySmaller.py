class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for item in nums:
            c = 0
            for val in nums:
                if val<item:
                    c+=1
            l.append(c)
        return l