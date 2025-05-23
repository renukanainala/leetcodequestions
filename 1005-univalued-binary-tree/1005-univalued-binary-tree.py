# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def solve(root,val1):
            if not root:
                return True
            if root.val!=val1:
                return False
            l=solve(root.left,val1) 
            r= solve(root.right,val1)
            return (l and r)
        return solve(root,root.val)
            