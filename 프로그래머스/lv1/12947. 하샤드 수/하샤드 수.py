def solution(x):
    div = sum([int(i) for i in str(x)])
    return x % div == 0