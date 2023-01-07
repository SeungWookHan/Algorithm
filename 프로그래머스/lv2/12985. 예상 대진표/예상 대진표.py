def solution(n,a,b):
    cnt = 0
    while a != b:
        a, b = (a // 2) + (a % 2), (b // 2) + (b % 2)
        cnt += 1
    return cnt