from functools import reduce

def solution(arr):
    return reduce(lambda a, b: a + b, arr) / len(arr)