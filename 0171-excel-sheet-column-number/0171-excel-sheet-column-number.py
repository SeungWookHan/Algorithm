class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def getNumber(t) -> int:
            return ord(t) - 64
        multiple = 1
        result = 0
        for t in columnTitle:
            result = result * 26 + getNumber(t)
        return result