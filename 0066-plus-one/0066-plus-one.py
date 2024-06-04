class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        digit = 1
        for i in range(len(digits)-1, -1, -1):
            sum += digits[i] * digit
            digit *= 10
        sum += 1
        return [int(x) for x in str(sum)]