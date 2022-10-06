def solution(n):
    a = [int(i) for i in str(n)]
    a.sort(reverse=True)
    return int("".join(map(str, a)))