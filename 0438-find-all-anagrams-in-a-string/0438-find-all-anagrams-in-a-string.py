class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        res, charP, charS = [], [0]*26, [0]*26
        
        for c in p:
            charP[ord(c)-ord('a')] += 1
        
        for i in range(0, len(s) - len(p) + 1):
            if i == 0: 
                for j in range(i, i + len(p)):
                    charS[ord(s[j]) - ord('a')] += 1       
            else: 
                charS[ord(s[i+len(p)-1]) - ord('a')] += 1
                
            if charS == charP:
                res.append(i)
            
            charS[ord(s[i]) - ord('a')] -= 1
            
        return res