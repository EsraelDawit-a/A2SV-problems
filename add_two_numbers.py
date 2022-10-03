# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = ""

        while l1  is not None:
            st1= str(l1.val)+st1
            l1 = l1.next
        
        st2 = ""
        while l2 is not None:
            st2= str(l2.val)+st2
            l2 = l2.next

        tot = str(int(st1)+int(st2))[::-1]
        
        new_l = ListNode(0)
        head = new_l

        for i in tot:
            node = ListNode(i)
            head.next = node
            head = head.next
         
        return new_l.next

         