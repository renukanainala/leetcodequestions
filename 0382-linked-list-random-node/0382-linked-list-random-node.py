# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head=head
        self.a=self.build(head)
        self.n=len(self.a)
    def build(self,head):
        t=head
        a=[]
        while t:
            a.append(t.val)
            t=t.next
        return a
    def getRandom(self) -> int:
        i=random.randint(0,self.n-1)
        return self.a[i]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()