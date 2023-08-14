class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        What the hell is a level?
        A level will be the 'depth' of each cell which cooresponds to it's distance
        to the nearest rotten orange.
        Looking at EX. 1,
        the levels are (level depth -> coordinates in mat)...
        0 -> (0,0)
        1 -> (0,1), (1,0)
        2 -> (0,2), (1,1)
        3 - > (2,1)
        4 -> (2,2)
        """
        # Defining grid bounds
        rows, cols = len(grid), len(grid[0])
        # Making queue
        queue = []
        # Making set
        seen = set()
        """We will use zero_count to count the number of empty cells in the grid to see if any fresh
        oranges remain"""
        zero_count = 0
        
        """ Iterate through grid and add any rotting oranges to queue and seen
        also, add any zeros to zero_count"""
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    seen.add((r,c))
                elif grid[r][c] == 0:
                    zero_count += 1
        
        # minutes will hold the min amount of time it takes for all oranges to rot (this will be the num of levels)
        minutes = 0
        # While queue is non empty
        while queue:
            # Iterate over each level (needed since we will append to the queue within each level iteration)
            for level_cell in range(len(queue)):
                # Dequeue the coordinates cooresponding with this level
                r, c = queue.pop(0)
                # Iterate through each neighbour
                for x, y in [(1,0), (-1,0), (0, 1), (0, -1)]:
                    newR, newC = r+x, c+y
                    # Skip neighbour if they are out of bounds, = to 0, or have already been seen
                    if (newR, newC) in seen or newR < 0 or newR >= rows or newC < 0 or newC >= cols or grid[newR][newC] == 0:
                        continue
                    # If this line is reached, the neighbour is a fresh orange that is unseen
                    # Append it's coordinates to the queue and add it to seen
                    queue.append((newR, newC))
                    seen.add((newR, newC))
            # If the queue is non-empty, increment minutes (weird edge case, maybe a better way to do this)
            if queue:
                minutes += 1
        """If the sum of the number of grid cells in seen (cooresponding to fresh and rotten oranges) and
        zero_count is < the total amount of grid cells in grid. There were untouched fresh oranges so impossible"""
        if len(seen) + zero_count < rows*cols:
            return -1
        # Else successful and return the number of levels iterated through (minutes)
        return minutes
                    