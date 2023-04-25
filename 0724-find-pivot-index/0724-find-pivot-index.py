class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, v in enumerate(nums):
            right_sum = total_sum - left_sum - v
            
            if right_sum == left_sum:
                return i
            left_sum += v
            
        return -1