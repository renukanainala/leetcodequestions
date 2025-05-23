# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.max1=float('inf')
        self.max2=float('inf')
        def solve(root):
            if not root:
                return 
            if root.val<self.max1:
                self.max2=self.max1
                self.max1=root.val
            if root.val<self.max2 and root.val>self.max1:
                self.max2=root.val
            solve(root.left)
            solve(root.right)
        solve(root)
        return self.max2 if self.max2!=float('inf') else -1