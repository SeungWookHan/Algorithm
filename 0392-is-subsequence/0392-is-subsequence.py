class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s > len_t:
            return False
        if len_s == 0:
            return True
        
        subsequence = 0
        for _t in t:
            if subsequence < len(s) and _t == s[subsequence]:
                subsequence += 1
        return subsequence == len(s)
            