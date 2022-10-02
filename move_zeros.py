class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        c = 0
        while i < len(nums)-1 and c <len(nums) -1 :
            if nums[i] == 0:
                nums.append(nums.pop(i))
                c+=1
            else:
                i+=1