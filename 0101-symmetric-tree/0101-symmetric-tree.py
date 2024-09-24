# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(r, l):
            if not r and not l:
                return True
            if not r or not l:
                return False
            return r.val == l.val and dfs(r.left, l.right) and dfs(r.right, l.left)
        
        return dfs(root.left, root.right)