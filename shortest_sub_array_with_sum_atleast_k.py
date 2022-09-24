class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixsum = [0]
        monoq = deque()
        minLen = float('inf')
        for n in nums:
            prefixsum.append(n+prefixsum[-1])
        for idx, cur in enumerate(prefixsum):
            
            while monoq and prefixsum[monoq[-1]] >= cur: monoq.pop() 
            while monoq and cur-prefixsum[monoq[0]]>=k: 
                minLen = min(minLen, idx-monoq.popleft())
            monoq.append(idx)
        return -1 if minLen == float('inf') else minLen