def solution(s):
    stack = []
    
    for s_ in s:
        if len(stack) == 0 and s_ == ")":
            return False
        if s_ == "(":
            stack.append(s_)
        else:
            stack.pop()

    return stack == []