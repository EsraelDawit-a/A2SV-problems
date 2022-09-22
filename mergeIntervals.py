class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 1 -> 2 -> 3 -> 6 -> 8 -> 10 -> 15 -> -> 18 
        
        intervals.sort()
        i = 1
        while i<=len(intervals)-1:
            if intervals[i][0] <= intervals[i-1][1]:
                
                #[[1,3],[2,6]] =>  2<=3 => [1,max(3,6)] 
                
                intervals[i] = [intervals[i-1][0],max(intervals[i][1],intervals[i-1][1])]
                
                # remove interval computed before pop(i-1) or intervals = intervals[0:]
                
                intervals.pop(i-1)
                
            else:
                i+=1
        return (intervals)