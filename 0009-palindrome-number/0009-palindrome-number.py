class Solution:
    def isPalindrome(self, x: int) -> bool:
        _x = str(x)[::-1]
        return str(x) == _x
        