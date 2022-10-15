def solution(arr1, arr2):
    return [[a1_ + a2_ for a1_, a2_ in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]