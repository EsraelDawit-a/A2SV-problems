class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        x,y = len(grid)-1,len(grid[0])-1
        
        # Sliding window with Prefix sum
        # pattern to find the sum
        # s = grid[0][0]+grid[0][1]+grid[0][2]+grid[1][1]+grid[2][0]+grid[2][1]+grid[2][2]
        max_sum = 0
        for i in range(1,x):
            for j in range(1,y):
                top = (grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1])
                middle = grid[i][j]
                bottom = grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1]
                
                max_sum = max(max_sum,(top+middle+bottom))
        
        return max_sum
                
                
            
