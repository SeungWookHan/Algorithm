class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        max_int = 2**31 - 1
        largest_power_of_three = 1
        while largest_power_of_three * 3 <= max_int:
            largest_power_of_three *= 3
        return largest_power_of_three % n == 0