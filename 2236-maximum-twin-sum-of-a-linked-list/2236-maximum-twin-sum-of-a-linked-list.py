# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            prev=None
            temp=head
            while temp:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            return prev
        def middle(head):
            slow=head
            fast=head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            return slow.next
        node=middle(head)
        head2=reverse(node)
        temp1=head
        temp2=head2
        s=0
        while temp2:
            s=max(s,temp1.val+temp2.val)
            temp1=temp1.next
            temp2=temp2.next
        reverse(head2)
        return s
        