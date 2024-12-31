# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        temp=dummy
        cur=head.next
        s=0
        while cur:
            s+=cur.val
            if cur.val==0:
                temp.next=ListNode(s)
                s=0
                temp=temp.next
            cur=cur.next
        return dummy.next