class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        hash_map = {0:1}

        for i in nums:
            cur_sum+=i
            dif = cur_sum - k
            
            res+= hash_map.get(dif,0)
            hash_map[cur_sum] = 1+hash_map.get(cur_sum,0)
            
        
        return res