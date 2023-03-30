from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            queue = deque()
            queue.append([sr, sc])

            while queue:
                x, y = queue.popleft()
                image[x][y] = color

                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < row and 0 <= ny < col and image[nx][ny] == origin_color:
                        queue.append((nx, ny))
        origin_color = image[sr][sc]
        row, col = len(image), len(image[0])
        if origin_color != color:
            dfs(sr, sc)
        return image