"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        h={};d=Node(-1);d1=d
        while temp:
            node=Node(temp.val)
            h[temp]=node
            d1.next=node
            d1=d1.next
            temp=temp.next
        temp=head
        while temp:
            if  temp.random:
                h[temp].random=h[temp.random]
            else:
                h[temp].random=None

            temp=temp.next
        return d.next

            