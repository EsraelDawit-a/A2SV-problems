class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
       car_load = [0]*1001
       stop = 0

       for trip,s,e in trips:
           car_load[s]+=trip
           car_load[e]-=trip
           stop = max(stop,e)

       load = 0
       for i in range(stop):
           load+=car_load[i]
           if load > capacity:
               return False
            
       return True
       


           

                
                    

