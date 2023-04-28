class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = dict()
        
        for a, b in zip(s, t):
            if hash.get(a) is None and b not in hash.values():
                hash[a] = b
        
        check = ""
        for i in s:
            if hash.get(i) is None:
                return False
            check += hash.get(i)
        return check == t
        
        