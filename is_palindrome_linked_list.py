# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head)->str:
        self.s = head
        self.l = []
        self.l.append(self.s.val)
        self.curr = self.s.next
        while self.curr is not None:
            self.l.append(self.curr.val)
            self.curr = self.curr.next
            
        if self.l==self.l[::-1]:
            return True
        else:
            return False