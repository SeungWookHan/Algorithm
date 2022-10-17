def solution(d, budget):
    count = 0
    # if sum(d) <= budget:
    #     return len(d)
    for i in sorted(d):
        if budget - i >= 0:
            count += 1
            budget -= i
    return count