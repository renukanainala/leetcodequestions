# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while a>0 and b>0:
                if a<b:
                    b=b%a
                else:
                    a=a%b
            if a==0:
                return b
            else:
                return a
        temp=head
        while temp and temp.next:
            val=gcd(temp.val,temp.next.val)
            node=ListNode(val);
            node.next=temp.next
            temp.next=node
            temp=node.next
        return head
