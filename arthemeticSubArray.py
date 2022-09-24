class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def isArthemetic(arr):
            d = arr[1]-arr[0]
            for i in range(2,len(arr)):
                if arr[i]-arr[i-1] !=d:
                    return False
            return True
                
        n = []       
        for l,r in zip(l,r):
            subA = nums[l:r+1]
            n.append(isArthemetic(sorted(subA)))
            
        return n
        