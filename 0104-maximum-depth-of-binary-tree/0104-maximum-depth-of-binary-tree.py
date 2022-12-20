# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = []
        depth = 0
        queue.append(root)
        queue.append(None)
        
        while queue:
            curr = queue.pop(0)
            if curr == None:
                depth += 1
                queue.append(None)
                if queue[0] == None:
                    break
                continue
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return depth