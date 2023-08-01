# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = []
        d = {}
        q.append([root, 0])
        
        if not root:
            return None
        isLeft = False
        isNoRight = False
        while q:
            curr, line = q.pop(0)
            d[line] = curr.val
            
            if curr.left:
                q.append([curr.left, line+1])
            # overwrites left if it exists
            if curr.right:
                q.append([curr.right, line+1])
        for k in sorted(d):
            res.append(d[k])
        return res
            