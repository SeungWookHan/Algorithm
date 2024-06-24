class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start, max_length = 0, 1
        
        def expand_around_center(left:int, right:int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        for i in range(len(s)):
            len1 = expand_around_center(i, i)
            len2 = expand_around_center(i, i+1)
            length = max(len1, len2)
            
            if length > max_length:
                start = i - (length - 1) // 2
                max_length = length
        return s[start:start + max_length]