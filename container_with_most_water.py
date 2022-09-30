class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp,rp,ans = 0,len(height)-1,0

        while lp < rp:
            he = min(height[lp],height[rp])
            width = rp-lp
            
            # Area of rectangle/square == height * width
            ans = max(ans, he * width)

            if height[lp] > height[rp]:
                rp-=1
            else:
                lp+=1
        return ans  
        