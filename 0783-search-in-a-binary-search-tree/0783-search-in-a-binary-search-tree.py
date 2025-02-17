# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        def preorder(cur,ans):
            if not cur:
                return
            ans.append(cur.val)
            preorder(cur.left,ans)
            preorder(cur.right,ans)
        cur=None
        while root:
            if root.val==k:
                cur=root
                break
            elif root.val>k:
                root=root.left
            else:
                root=root.right
        ans=[cur]
        #preorder(cur,ans)
        return cur