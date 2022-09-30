class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        st = []
        
        for i in range(len(temperatures)):
            while st and st[-1][0]<temperatures[i]:
                va,ind = st.pop()
                out[ind] = i-ind

            st.append((temperatures[i],i))

        return out