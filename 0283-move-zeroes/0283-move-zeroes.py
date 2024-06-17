class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == [0]:
            return [0]
        last_non_zero_found_at = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0