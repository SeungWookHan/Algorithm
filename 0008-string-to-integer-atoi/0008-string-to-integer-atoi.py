class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        result = 0
        sign = 1
        started = False
        
        for c in s:
            if c == ' ' and not started:
                continue
            elif c == '-' and not started:
                sign = -1
                started = True
            elif c == '+' and not started:
                started = True
            elif c.isdigit():
                result = result * 10 + int(c)
                started = True
                # Overflow check
                if sign * result < MIN_INT:
                    return MIN_INT
                if sign * result > MAX_INT:
                    return MAX_INT
            else:
                break
        return sign * result