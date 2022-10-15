def solution(s):
    answer = ""
    arr = s.split(" ")
    for a in arr:
        for i, x in enumerate(a):
            answer += x.upper() if i % 2 == 0 else x.lower()
        answer += " "
    return answer[:-1]