# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, o: TreeNode, c: TreeNode, t: TreeNode) -> TreeNode:
            res=None
            def inorder(root,c):
                nonlocal res
                if not root:
                    return
                res=inorder(root.left,c.left)
                if res:
                    return res
                if root==t:
                    return c
                return inorder(root.right,c.right)
            return inorder(o,c)
            