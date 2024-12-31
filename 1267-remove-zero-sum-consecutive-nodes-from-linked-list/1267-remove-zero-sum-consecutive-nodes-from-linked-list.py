# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        temp=head
        h={}
        s=0
        h[s]=dummy
        while temp:
            s+=temp.val
            if s in h:
                node=h[s]
                t2=node.next
                s1=s
                while t2!=temp:
                    s1+=t2.val
                    del h[s1]
                    t2=t2.next
                node.next=temp.next
            else:
                h[s]=temp
            temp=temp.next
        return dummy.next