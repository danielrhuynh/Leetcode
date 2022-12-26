class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r,c):
            queue = []
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if ((row+dr) in range(ROWS) and (col+dc) in range(COLS) and grid[row+dr][col+dc] == '1' and (row+dr, col+dc) not in visited):
                        queue.append((row+dr, col+dc))
                        visited.add((row+dr, col+dc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
                    