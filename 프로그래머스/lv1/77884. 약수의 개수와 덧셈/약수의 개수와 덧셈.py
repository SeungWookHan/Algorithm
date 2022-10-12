def sign(num):
    return -1 if int(num**0.5) == num**0.5 else 1
def solution(left, right):
    return sum([i * sign(i) for i in range(left, right + 1)])