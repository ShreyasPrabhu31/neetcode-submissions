class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 2147483647:
                        continue
                    
                    grid[row][col] = grid[r][c] + 1
                    q.append([row, col])