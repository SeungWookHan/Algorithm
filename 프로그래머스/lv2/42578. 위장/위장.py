def solution(clothes):
    hash = {}
    answer = 1

    for _, key in clothes:
        if hash.get(key) is not None:
            hash[key] += 1
        else:
            hash[key] = 1
    for value in hash.values():
        answer *= (value + 1)
    return answer - 1