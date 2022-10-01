'''
 using two pointer method fast pointer and slow 
 fast goes 2x faster than slow pointer so at the time 
 fast pointer reaches the end the slow will be at the middle 

'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head

        while fast and fast.next is not None:
            fast,slow = fast.next.next,slow.next

        return slow