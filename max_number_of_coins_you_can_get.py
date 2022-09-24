class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l,r = 0,len(piles)-1
        s = 0
        print(piles)
        while r>l:
            l+=1
            s+=piles[r-1]
            r-=2
        return s


            