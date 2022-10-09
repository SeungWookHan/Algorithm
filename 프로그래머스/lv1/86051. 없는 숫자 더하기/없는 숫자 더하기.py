# from collections import Counter

# def solution(numbers):
#     sum = 0
#     counter = Counter(numbers)
#     for i in range(0, 10):
#         if i not in counter:
#             sum += i
#     return sum

def solution(numbers):
    return 45 - sum(numbers)