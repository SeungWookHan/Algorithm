from collections import deque

def check(s):
    d = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if stack:
                top = stack.pop()
                if d[c] != top:
                    return False
            else:
                return False
    return len(stack) == 0

def solution(s):
    answer = 0
    deq = deque(s)
    
    for _ in range(len(deq)):
        deq.rotate(-1)
        if check(deq):
            answer += 1
    return answer