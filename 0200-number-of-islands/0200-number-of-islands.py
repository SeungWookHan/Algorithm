class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < row and 0 <= j < col and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i, j - 1)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i + 1, j)
                return 1
            return 0
        count = sum(dfs(i, j) for i in range(row) for j in range(col))
        return count