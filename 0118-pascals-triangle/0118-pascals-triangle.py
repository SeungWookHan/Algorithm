class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        result = [[1], [1,1]]
        while len(result) < numRows:
            last_row = result[-1]
            new_row = [1]
            for i in range(1, len(last_row)):
                new_row.append(last_row[i-1]+last_row[i])
            new_row.append(1)
            result.append(new_row)
        return result