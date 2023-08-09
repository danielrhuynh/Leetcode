"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Mapping old nodes to new node
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                # Returns new node (the copy)
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbour in node.neighbors:
                copy.neighbors.append(dfs(neighbour))
            return copy
        return dfs(node) if node else None