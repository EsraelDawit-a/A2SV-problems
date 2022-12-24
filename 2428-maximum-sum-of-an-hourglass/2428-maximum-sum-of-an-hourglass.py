class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        x,y = len(grid)-2,len(grid[0])-2
        
        
        # pattern to find the sum
        # s = grid[0][0]+grid[0][1]+grid[0][2]+grid[1][1]+grid[2][0]+grid[2][1]+grid[2][2]
        max_sum = 0
        # only check upto  len(grid)-1 for x and for y starting from index 1 len(grid)-1
        # only check upto len(grid)-2 for x and y starting from index 0
        for i in range(x):
            for j in range(y):
             
                top = (grid[i][j]+grid[i][j+1]+grid[i][j+2])
                middle = grid[i+1][j+1]
                bottom = grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                
                max_sum = max(max_sum,(top+middle+bottom))
         
        return max_sum
                
                
            
                
            
