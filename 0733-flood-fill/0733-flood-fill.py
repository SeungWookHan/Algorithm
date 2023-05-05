from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r_max = len(image)
        c_max = len(image[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        def dfs(image, r, c, newColor, color):
            if not (0 <= r < r_max and 0 <= c < c_max and image[r][c] == color):
                return
            image[r][c] = newColor
            for d in directions:
                dfs(image, r+d[0], c+d[1], newColor, color)
        
        color = image[sr][sc]
        if color == newColor:
            return image
        dfs(image, sr, sc, newColor, color)
        return image