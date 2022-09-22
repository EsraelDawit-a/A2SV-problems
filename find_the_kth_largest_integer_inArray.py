'''
  just change the number to int and pass it to lambda functions 
  to sort it with custom sorting key
'''

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda x:int(x),reverse=True)
        return nums[k-1]
        