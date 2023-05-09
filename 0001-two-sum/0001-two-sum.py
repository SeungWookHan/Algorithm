class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # value: idx
        
        for idx, v in enumerate(nums):
            rest = target - v
            if rest in hash_map:
                return [hash_map[rest], idx]
            hash_map[v] = idx
            