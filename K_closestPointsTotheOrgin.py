from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
         use Eculidian distance to sort and Lambda function
        '''
        
        sort_key = lambda pt: (sqrt( (pt[0]*pt[0]) + ( pt[1]*pt[1] ) ))
        
        points.sort(key = sort_key )
        
        return points[:k]
        