# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def paths(root,p):
            if not root:
                return
            if not root.left and not root.right:
                p.append(str(root.val))
                ans.append("->".join(p))
                p.pop()
                return            
            p.append(str(root.val))
            paths(root.left,p)
            paths(root.right,p)
            p.pop()
        if not root:
            return []
        paths(root,[])
        return ans