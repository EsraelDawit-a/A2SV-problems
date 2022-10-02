# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        try:
            prev,node = head,head.next

            while prev.next is not None:
                if prev.val == node.val:
                    prev.next = node.next
                    node = node.next
                
                else:
                    temp = node
                    node = node.next
                    prev = temp

            return head
        except:
            return head