# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        q.append((root,1))
        s=float('-inf')
        minlevel=float('inf')
        while q:
            n=len(q)
            t=0
            for i in range(n):
                e,currentlevel=q.popleft()
                t+=e.val
                if e.left:
                    q.append((e.left,currentlevel+1))
                if e.right:
                    q.append((e.right,currentlevel+1))
            if t>s:
                s=t
                minlevel=currentlevel
                
        return minlevel


                


