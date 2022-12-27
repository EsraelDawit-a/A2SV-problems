class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # take the string with minimum length "flow"
        min_length_string = min(strs,key=len) 
        
        for word in strs:
            
            while len(min_length_string) > 0:
                # if the word is staring with the minimum 
                # string the maximum we can get
                # is only that
                if word.startswith(min_length_string):
                    break
                # else we can remove the last character of
                # the minimum length string and cheack again
                else:
                    min_length_string = min_length_string[:-1] 
        
        return min_length_string
        