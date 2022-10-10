# def solution(a, b):
#     result = 0
#     for a_, b_ in zip(a, b):
#         result += a_ * b_
#     return result

def solution(a, b):
    return sum([a_ * b_ for a_, b_ in zip(a, b)])