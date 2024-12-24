# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev=None
        self.mini=float('inf')
        def inorder(root):
            nonlocal prev
            if not root:
                return
            inorder(root.left)
            if  prev:
                self.mini=min(self.mini,root.val-prev.val)
            prev=root
            #mini=min()
            inorder(root.right)
        inorder(root)
        return self.mini