class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []

        for i in num:
            while st and st[-1] > i and k:
                st.pop()
                k-=1
            if st or i is not '0':
                st.append(i)
        
        if k:
            st = st[0:-k]

        return ''.join(st) if st else "0"

        