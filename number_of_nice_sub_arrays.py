class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):

            if nums[i]%2 == 0:

                nums[i] = 0

            else:

                nums[i] = 1

        

    

        res = 0
        cur_sum = 0
        prefix_sum_map = {0:1}

        for n in nums:

            cur_sum+=n

            dif = cur_sum-k

            res+=prefix_sum_map.get(dif,0)

            prefix_sum_map[cur_sum] = 1+prefix_sum_map.get(cur_sum,0)

        

        return res



        



        