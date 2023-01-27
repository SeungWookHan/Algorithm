def solution(t, p):
    answer = 0
    len_p = len(p)
    for i in range(len(t)):
        check_num = t[i:i + len_p]
        if len(check_num) == len_p and check_num <= p:
            answer += 1
    return answer