class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hash_table:
                return [i, hash_table[rest]]
            hash_table[nums[i]] = i