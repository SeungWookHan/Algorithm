from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        m, n = len(s), len(p)
        if m < n:
            return answer
        s_counter = Counter(s[:n-1])
        p_counter = Counter(p)
        
        end=0 
        for end in range(n-1, m):
            start = end - (n-1)
            
            s_counter[s[end]] += 1
            if s_counter == p_counter:
                answer.append(start)
            
            s_counter[s[start]] -= 1
            if s_counter[s[start]] == 0:
                del s_counter[s[start]]
        return answer
        
        