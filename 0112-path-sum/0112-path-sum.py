# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        def path(root,c):
            if not root:
                return False
            c-=root.val
            if not root.left and not root.right:
                return c==0
            return (path(root.left,c) or path(root.right,c))
        return path(root,target)
        
       