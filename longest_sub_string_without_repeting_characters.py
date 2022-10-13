class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = ""
        l = 0
        wind = 0
        for i in range(len(s)):
            if s[i] in char_set:
                ind = char_set.index(s[i])
                char_set = char_set[ind+1:]
                l+=ind+1
            char_set+=(s[i])
            wind = max(wind,i-l+1)
            
        
        return wind
