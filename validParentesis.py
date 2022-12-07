class Solution:
    #stack implementaion
    def isValid(self, s: str) -> bool:
        st = []
        c = 0
        for i in range(len(s)):
            if s[i] =="{":
                st.append('}')
                c+=1
            elif s[i] =="[":
                st.append(']')
                c+=1
            elif s[i] =="(":
                st.append(')')
                c+=1
            elif len(st) > 0 and  s[i] == st[-1]:
                st.pop()
                c+=1
            
            
       
        return True if len(st) == 0 and c == len(s) else False
            
