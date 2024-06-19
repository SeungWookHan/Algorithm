class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
        
        for i, c in enumerate(s):
            if char_count[c] == 1:
                return i
        return -1