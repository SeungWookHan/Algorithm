def solution(s):
    answer = ''
    num = list(map(int, s.split(" ")))
    num.sort()
    answer += str(num[0]) + " "
    answer += str(num[-1]) 
    return answer