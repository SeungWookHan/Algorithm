class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = [s.strip() for s in s.split()]
        return len(result.pop())