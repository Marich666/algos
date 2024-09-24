# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = collections.deque([root])
        while q:
            summa = 0
            len_lvl = len(q)

            for _ in range(len_lvl):
                node = q.popleft()
                summa += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(summa/len_lvl)
            
        return res