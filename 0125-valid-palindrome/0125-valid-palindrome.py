class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''.join([i.lower() for i in s if i.isalnum()])
        return strs == strs[::-1]
                
            