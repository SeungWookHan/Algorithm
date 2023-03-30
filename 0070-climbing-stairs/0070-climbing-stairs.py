class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        climb = [0 for i in range(n)]
        climb[0] = 1
        climb[1] = 2
        
        for i in range(2, n):
            climb[i] = climb[i-1] + climb[i-2]
        return climb[n-1]