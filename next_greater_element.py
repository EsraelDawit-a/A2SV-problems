class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for it in nums1:
            try:
                got_one = False
                for i in range(nums2.index(it)+1,len(nums2)):
                    if nums2[i] > it:
                        l.append(nums2[i])
                        got_one = True
                        break
                if got_one == False:
                    l.append(-1)
                
              
            except:
                l.append(-1)
        return l