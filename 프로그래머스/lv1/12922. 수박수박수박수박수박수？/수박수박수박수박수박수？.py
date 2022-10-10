def solution(n):
    quotient = n // 2
    return "수박" * quotient if n % 2 == 0 else "수박" * quotient + "수"