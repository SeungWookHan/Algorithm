class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if i == ")":
                    if temp != "(":
                        return False
                elif i == "}":
                    if temp != "{":
                        return False
                elif i == "]":
                    if temp != "[":
                        return False
        return len(stack) == 0