def solution(s, n):
    answer = ""
    for s_ in s:
        if s_ != " ":
            c = ord(s_) + n
            if s_.isupper():
                answer += chr((c - ord('A')) % 26 + ord('A'))
            else:
                answer += chr((c - ord('a')) % 26 + ord('a'))
        else:
            answer += " "
    return answer