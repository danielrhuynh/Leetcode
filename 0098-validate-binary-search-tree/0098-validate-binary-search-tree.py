# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidNode(node, l, h):
            if not node:
                return True
            if not (node.val < h and node.val > l):
                return False
            return isValidNode(node.left, l, node.val) and isValidNode(node.right, node.val, h)
        low = -2**31-1
        high = 2**31
        return isValidNode(root, low, high)
            
        