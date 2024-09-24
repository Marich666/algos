# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def builder(left, right):
            mid = (right + left) // 2
            root = TreeNode(nums[mid])
            if mid-1 >= left:
                root.left = builder(left, mid-1)
            if mid+1 <= right:
                root.right = builder(mid+1, right)
            return root

        return builder(0, len(nums)-1)
            