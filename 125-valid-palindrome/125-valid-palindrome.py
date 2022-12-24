import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # replace only characters that are not number or alphabet [^a-z0-9]
        s = re.sub("[^a-z0-9]", "", s.lower())
        l,r = 0,len(s)-1
        
        while l<r:
            if s[l] !=s[r]:
                return False
            l+=1
            r-=1
        return True
            