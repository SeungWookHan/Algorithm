from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    c = c.most_common()
    for _, val in c:
        if k <= 0:
            return answer
        k -= val
        answer += 1
    return answer