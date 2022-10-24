from collections import Counter 

def solution(N, stages):
    dividend = len(stages)
    fail_list = {}
    for i in range(1, N + 1):
        if dividend != 0:
            count = stages.count(i)
            fail_list[i] = count / dividend
            dividend -= count
        else:
            fail_list[i] = 0
    print(fail_list)
    return sorted(fail_list, key=lambda x: fail_list[x], reverse=True)