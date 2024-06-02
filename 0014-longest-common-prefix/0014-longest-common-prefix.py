class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        for i, c in enumerate(shortest_str):
            for other in strs:
                if other[i] != c:
                    return shortest_str[:i]
        return shortest_str