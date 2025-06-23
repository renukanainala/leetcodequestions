# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            temp=head
            prev=None
            while temp:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
        def findkthnode(temp,k):
            c=0
            while temp and c<k-1:
                temp=temp.next
                c+=1
            return temp
        temp=head
        kth=head
        prev=None
        while temp:
            kth=findkthnode(temp,k)
            if kth is None:
                if prev:
                    prev.next=temp
                break
            nextgroup=kth.next
            kth.next=None
            reverse(temp)
            if temp==head:
                head=kth
            else:
                prev.next=kth
            prev=temp
            temp=nextgroup
        return head
            
       