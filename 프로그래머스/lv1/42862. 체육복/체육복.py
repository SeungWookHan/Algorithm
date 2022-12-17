def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for r in set_reserve:
        if r-1 in set_lost:
            set_lost.remove(r-1)
        elif r+1 in set_lost:
            set_lost.remove(r+1)
    return n - len(set_lost)