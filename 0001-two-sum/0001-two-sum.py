class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} # value: index
        
        for idx, value in enumerate(nums):
            rest = target - value
            if rest in hash_table:
                return [hash_table[rest], idx]
            else:
                hash_table[value] = idx
            