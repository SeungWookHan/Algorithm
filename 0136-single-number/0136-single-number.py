class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums == [1]:
            return 1
        num_map = {}
        for n in nums:
            if n in num_map:
                del num_map[n]
            else:
                num_map[n] = True
        return list(num_map.keys())[0]