'''
  if a car reaches target before Another car , it will intersect or reach that car before reaching the target
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        for p,s in sorted(zip(position,speed))[::-1]:
            st.append((target-p)/s)
            if len(st) >=2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)
