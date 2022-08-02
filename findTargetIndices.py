class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = sorted(nums)
        ans = []
        for i in range(len(l)):
            if l[i] == target:
                ans.append(i)
        return ans