class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Use recursive dfs approach, you could also use an iterative bfs approach
        rows, cols = len(image), len(image[0])
        
        def dfs(row, col, startColor):
            # Base case is when the coordinate is out of range
            if (row >= rows or row < 0 or col >= cols or col < 0 or image[row][col] != startColor):
                return
            image[row][col] = color
            return dfs(row-1, col, startColor), dfs(row+1, col, startColor), dfs(row, col-1, startColor), dfs(row, col+1, startColor)
        # Make sure the work is not already done to avoid being in a loop
        if image[sr][sc] != color:
            dfs(sr, sc, image[sr][sc])
        return image
            
            