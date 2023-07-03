class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(len(nums)):
            if nums[0] == val:
                del nums[0]
            else:
                nums.append(nums[0])
                del nums[0]
        return len(nums)
                