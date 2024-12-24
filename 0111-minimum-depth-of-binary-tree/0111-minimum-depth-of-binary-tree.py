# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans=[]
        l=float('inf')
        def path(root,d):
            nonlocal l
            if not root:
                return
            if not root.left and not root.right:
                l=min(l,d)
            else: 
                path(root.left,d+1)
                path(root.right,d+1)
        if not root:
            return 0
        path(root,1)
        #print(ans)
        return l