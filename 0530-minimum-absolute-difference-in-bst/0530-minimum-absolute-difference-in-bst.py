# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            values.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        values = []
        dfs(root)
        values.sort()
        res = values[1] - values[0]
        for i in range(2, len(values)):
            res = min(values[i]-values[i-1], res)
        return res