# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node,prev,temp = head,None,None

        while node:
            temp = node
            node =node.next
            temp.next = prev
            prev = temp
            


        return temp
