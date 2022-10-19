# from itertools import combinations

# def solution(nums):
#     dividend = len(nums) // 2
#     return max([len(list(set(i))) for i in combinations(nums, dividend)])

def solution(nums):
    number_of_unique = len(list(set(nums)))
    number_of_choose = len(nums) // 2
    if number_of_choose > number_of_unique:
        return number_of_unique
    return number_of_choose