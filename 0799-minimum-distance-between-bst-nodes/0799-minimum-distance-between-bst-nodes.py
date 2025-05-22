# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.val1=-1
        self.d=float('inf')
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.val1!=-1:
                self.d=min(self.d,abs(self.val1-root.val))
            self.val1=root.val
            inorder(root.right)
        inorder(root)
        return self.d 