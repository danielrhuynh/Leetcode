# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def preOrder(root):
            if root.left:
                preOrder(root.left)
            res.append(root)
            if root.right:
                preOrder(root.right)
        preOrder(root)
        return res[k-1].val