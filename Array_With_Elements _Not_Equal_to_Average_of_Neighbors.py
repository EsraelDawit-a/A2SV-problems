'''
 # Hint 1: A number can be the average of its neighbors if one neighbor is smaller than the number and the other is greater than the number.
 
 # Hint 2: We can put numbers smaller than the median on odd indices and the rest on even indices.
 
'''


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        mid = nums[len(nums)//2]
        new_list = [0]*len(nums)

        odd = 1
        even = 0
        for i in range(len(nums)):
            
            if nums[i] < mid:
                new_list[odd] = nums[i]
                odd+=2
            else:
                new_list[even] = nums[i]
                even+=2
        
        return new_list
        