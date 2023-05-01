from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        result = 0
        f = 0
        
        for _, v in Counter(s).items():
            if v % 2 == 0:
                result += v
            else:
                result += v-1
                f = 1
        return result + f