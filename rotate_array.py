
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k%len(nums)
        while n>0:
                nums.insert(0,nums.pop())
                n-=1
            

       
