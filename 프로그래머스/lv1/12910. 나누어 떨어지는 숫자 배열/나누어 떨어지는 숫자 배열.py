def solution(arr, divisor):
    res = [x for x in arr if x % divisor == 0]
    res.sort()
    if len(res) == 0:
        return [-1]
    return res