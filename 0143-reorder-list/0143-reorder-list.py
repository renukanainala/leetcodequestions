# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''def reverse(head):
            prev=None;temp=head
            while temp:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            return prev
        s=head;f=head;t=head
        while f.next and f.next.next:
            s=s.next
            f=f.next.next
        new=reverse(s.next)
        while new:
            t.next=new
            t=t.next
            new=new.next'''
        p2 = head
        values = []
        while p2:
            values.append(p2.val) #all  node values
            p2 = p2.next
        left, right = 0, len(values) - 1
        p1 = head

        while left <= right:
            p1.val = values[left]
            p1 = p1.next
            if p1 is not None:
                p1.val = values[right]
                p1 = p1.next
            left += 1
            right -= 1
        return head
            