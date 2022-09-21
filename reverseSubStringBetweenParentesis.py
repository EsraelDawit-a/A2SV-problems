class Solution:
    def reverseParentheses(self, s: str) -> str:
        '''
        s = "(ed(et(oc))el)"
        
        oc -> co
        etco -> octe
        
        ed-octe-el -> leetcode
        
        '''

        stac = []
        st = ""
        for i in range(len(s)):
            if s[i] != ")":
                stac.append(s[i])
            else:
                while stac[-1] !="(":
                    st+=stac[-1]
                    stac.pop()

                stac.pop()
                for k in st:
                    stac.append(k)

                st = ""

        return (''.join(stac))

                    
                
                
        
                    