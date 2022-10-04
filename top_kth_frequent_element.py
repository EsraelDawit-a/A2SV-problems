class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {}
        for num in nums:
            if num in Map:
                Map[num] += 1
            else:
                Map[num] = 1
        sort_c = sorted(Map.items(), key=lambda x:x[1], reverse= True)
        return [x[0] for x in sort_c[:k]]