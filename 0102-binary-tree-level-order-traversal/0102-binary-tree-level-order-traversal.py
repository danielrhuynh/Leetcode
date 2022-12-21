# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        
        queue.append(root)
        queue.append(None)
        temp = []
        while queue:
            curr = queue.pop(0)
            if curr == None:
                res.append(temp)
                queue.append(None)
                temp = []
                if queue[0] == None:
                    break
                continue
            temp.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return res