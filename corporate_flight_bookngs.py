class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        r = [0]*(n+1)

        # bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
        # Consider 1st booking: +10 at 1st stop and -10 at 3rd stop => [10,0,-10,0,0]
        # Consider 2nd booking: +20 at 2nd stop and -20 at 4th stop => [10,20,-10,-20,0]
        # Consider 3rd booking: +25 at 2nd stop and -25 at 6th stop=>[10,45,-10,-20,0,-25]
        
        '''
          So total passengers at each stop: 
          [10,10+45,10+45-10,10+45-10-20,10+45-10-20+0,10+45-10-20+0-25]= [10,55,45,25,25,0]
         '''   
        for f,l,s in bookings:
            
            r[f-1] += s
            r[l] += -s

        for i in range(1,n+1):
            r[i]+=r[i-1]    

        return (r[:-1])