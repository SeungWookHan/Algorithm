def solution(n):
    s = n ** 0.5
    return (s + 1) ** 2 if s == int(s) else -1