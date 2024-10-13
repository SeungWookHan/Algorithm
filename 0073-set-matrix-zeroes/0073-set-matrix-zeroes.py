class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_positions = []
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))
        
        for i, j in zero_positions:
            for c in range(cols):
                matrix[i][c] = 0
            for r in range(rows):
                matrix[r][j] = 0
        