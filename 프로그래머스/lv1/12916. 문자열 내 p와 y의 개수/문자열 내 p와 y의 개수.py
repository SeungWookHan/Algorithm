from collections import Counter

def solution(s):
    c = Counter(s.lower())
    return c['y'] == c['p']