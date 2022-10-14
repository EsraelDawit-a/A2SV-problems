class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the peoples
        # mark two pointers 0 and len(peoples)-1
        # if sum of two pointers > limit the largest pointer needs
        # its own boat
        # else both can fit

        people.sort()
        b,i,j = 0,0,len(people)-1
        while i <= j:
            if people[i] + people[j] >limit:
                j-=1 
            else:
                i+=1
                j-=1
            b+=1
        return b