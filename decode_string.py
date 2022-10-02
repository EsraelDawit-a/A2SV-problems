'''
  use stack
  
'''

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i]!="]":
                st.append(s[i])
            else:
                sub = ""
                while st[-1]!="[":
                    c = st.pop()
                    sub = c + sub
                st.pop()
                r = ""
                while st and st[-1].isdigit():
                    r = st.pop() + r
                st.append(int(r)*sub)

                
        return "".join(st)