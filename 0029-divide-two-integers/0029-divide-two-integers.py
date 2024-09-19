class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        quotient = quotient if sign == 1 else -quotient
        return max(-2**31, min(quotient, 2**31 - 1))
        