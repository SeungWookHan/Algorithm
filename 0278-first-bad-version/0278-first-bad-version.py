# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n < 2:
            return n
        left = 1
        right = n #5
        while left <= n:
            mid = (left + right) // 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid-1):
                right = mid-1
            else:
                left = mid+1
                
        
                