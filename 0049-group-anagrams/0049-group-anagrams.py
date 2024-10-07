from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            s_sorted = ''.join(sorted(s))
            anagrams[s_sorted].append(s)
        return list(anagrams.values())
            