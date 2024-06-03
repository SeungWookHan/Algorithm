class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pare = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in ("(", "{", "["):
                stack.append(i)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if p != pare[i]:
                    return False
        return len(stack) == 0