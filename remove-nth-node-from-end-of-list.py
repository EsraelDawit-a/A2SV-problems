'''
 first find length of the linked list c 
 then traverse once until reaching c-n which is the node to be deleted
 then remove the node
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node,c = head,1

        while node.next is not None:
            node = node.next
            c+=1

        r_node,prev,x = head,None,0
        while  x<c-n and r_node.next is not None:
            temp = r_node
            r_node = r_node.next
            prev = temp
            x+=1
       
        if prev is None:
           head = r_node.next
        else:
            prev.next = r_node.next
        return head
