class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipdict = dict()
        for a, b in zip(s, t):
            if zipdict.get(a) is None and b in zipdict.values():
                return False
            zipdict[a] = b
        compare = ""
        for i in s:
            compare += zipdict[i]
        if compare == t:
            return True
        return False