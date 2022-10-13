from itertools import combinations

# def solution(numbers):
#     answer = set()
#     for i in list(combinations(numbers, 2)):
#         answer.add(sum(i))
#     return sorted(answer)

def solution(numbers):
    return sorted(set([sum([i, j]) for i, j in combinations(numbers, 2)]))