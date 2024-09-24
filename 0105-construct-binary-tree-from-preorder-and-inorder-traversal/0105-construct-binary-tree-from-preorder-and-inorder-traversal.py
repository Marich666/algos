# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(st, end):
            if st > end:
                return None
            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]
            root.left = dfs(st, mid-1)
            root.right = dfs(mid+1, end)

            return root

        mapping = {}
        for i, v in enumerate(inorder):
            mapping[v] = i
        preorder = collections.deque(preorder)
        return dfs(0, len(inorder) - 1)

