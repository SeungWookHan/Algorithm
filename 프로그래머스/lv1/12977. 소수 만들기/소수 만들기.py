from itertools import combinations  

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    comb = [sum(i) for i in combinations(nums, 3)]
    answer = list(map(is_prime, comb)).count(True)
    return answer