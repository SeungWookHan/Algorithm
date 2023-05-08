class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or x > n-1 or y < 0 or y > m-1:
                return False
            if grid[x][y] == "1":
                grid[x][y] = "0"
                
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
                return True
            return False
                
        
        n, m = len(grid), len(grid[0])
        answer = 0
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j) == True:
                    answer += 1
        return answer