def solution(s):
    answer = ""
    lower_list = list(map(lambda x: x.lower(), s.split(" ")))
    for idx, lower in enumerate(lower_list):
        if idx < len(lower_list) - 1:
            answer += lower.capitalize() + " "
        else:
            answer += lower.capitalize()
    return answer