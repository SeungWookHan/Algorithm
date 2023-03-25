class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        length = 0
        center = False
        
        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                center = True
        
        if center:
            length += 1
        return length