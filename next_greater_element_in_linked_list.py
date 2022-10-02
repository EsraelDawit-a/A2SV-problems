# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
   * trick
      # use monotonic Stack concept  
'''
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        st = []
        arr = []
        node = head
        i = 0
        while node is not None:
            if len(st) == 0:
                arr.append(0)
                st.append((i,node.val))
                node = node.next
                i+=1
            elif st[-1][-1] < node.val:
                while st and st[-1][-1] < node.val: 
                    ind = st[-1][0]
                    arr[ind] = node.val
                    st.pop()
            else:
                arr.append(0)
                st.append((i,node.val))
                node = node.next
                i+=1
        return arr


