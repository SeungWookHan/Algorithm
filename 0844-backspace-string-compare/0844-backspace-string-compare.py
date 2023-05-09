class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for i in s:
            if i == "#" and stack_s:
                stack_s.pop()
            elif i != "#":
                stack_s.append(i)
            else:
                continue
        
        for i in t:
            if i == "#" and stack_t:
                stack_t.pop()
            elif i != "#":
                stack_t.append(i)
            else:
                continue
        
        return stack_s == stack_t