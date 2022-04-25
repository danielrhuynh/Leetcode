class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # base case
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c, oldColor, newColor):
            # Base case
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != oldColor or oldColor == newColor:
                return
            image[r][c] = newColor
            directions = [(1,0), (-1,0), (0, 1), (0, -1)]
            for d in directions:
                newRow, newCol = r+d[0], c+d[1]
                dfs(newRow, newCol, oldColor, newColor)
        
        dfs(sr, sc, image[sr][sc], newColor)
        return image
        