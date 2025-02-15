# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        l=dummy
        t1=h1 ;t2=h2;c=0
        while t1 or t2:
            s=c
            if t1:
                s+=t1.val
            if t2:
                s+=t2.val
            newnode=ListNode(s%10)
            c=s//10
            l.next=newnode
            l=l.next
            if t1:t1=t1.next
            if t2:t2=t2.next
        if c:
            l.next=ListNode(c)
        return dummy.next
            
            