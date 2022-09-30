class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        lp,rp,n = 0,0,len(pushed)
        st = []

        while lp < n or rp < n:
            if st and st[-1] == popped[rp]:
                st.pop()
                rp+=1
            elif lp < n :
                st.append(pushed[lp])
                lp+=1
            else:
                return False
        return True
