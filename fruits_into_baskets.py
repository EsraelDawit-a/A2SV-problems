class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash_map,i,mx = {},0,0

       
        # if the lenght of hash_map >2 means we have 3 diffrent items that is
        # not allowed so we will increment i to next item position and delete the
        # current item from the hash_map
        for j,f in enumerate(fruits):
            hash_map[f] = hash_map.get(f,0)+1
            if len(hash_map) > 2:
                hash_map[fruits[i]]-=1
                if hash_map[fruits[i]] == 0:
                    del hash_map[fruits[i]]
                i+=1
            mx = max(mx,j-i+1)
        return mx
            
        


            
        