def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    zero_count = lottos.count(0)
    none_zero_lottos = []
    if zero_count == 6: # 정해진 답, 미리 리턴
        return [1, 6]
    
    worst = len(list(set(lottos) & set(win_nums)))
    best = worst + zero_count
    return [rank[best], rank[worst]]