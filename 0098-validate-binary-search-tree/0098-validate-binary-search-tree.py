# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidNode(root, low, high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return isValidNode(root.left, low, root.val) and isValidNode(root.right, root.val, high)
        return isValidNode(root, -2**31-1, 2**31)
        