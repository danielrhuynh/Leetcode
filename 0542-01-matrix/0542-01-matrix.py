class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # DFS solution times out so we try the BFS solution
        rows, cols = len(mat), len(mat[0])
        queue = []
        seen = set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    seen.add((i,j))
        level = 0
        while queue:
            for levelCell in range(len(queue)):
                r, c = queue.pop(0)
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newR = r + x
                    newC = c + y
                    if newR < 0 or newR >= rows or newC < 0 or newC >= cols or (newR, newC) in seen:
                        continue
                    # else we have found a one
                    queue.append((newR, newC))
                    seen.add((newR, newC))
                mat[r][c] = level
            level += 1
        return mat
                    
                    
            
            