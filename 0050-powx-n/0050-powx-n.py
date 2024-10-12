class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        is_neg = n < 0
        n = abs(n)
        result = 1
        
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return 1 / result if is_neg else result