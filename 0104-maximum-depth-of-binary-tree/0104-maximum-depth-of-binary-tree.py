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
        q = []
        q.append(root)
        q.append(None)
        depth = 0
        
        while q:
            curr = q.pop(0)
            if curr == None:
                depth += 1
                q.append(None)
                if q[0] == None:
                    return depth
                continue
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return depth