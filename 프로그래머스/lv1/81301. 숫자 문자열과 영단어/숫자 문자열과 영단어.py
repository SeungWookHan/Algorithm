def solution(s):
    number_hash = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    answer = ""
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            if s[i:i+3] in number_hash:
                answer += number_hash[s[i:i+3]]
                i += 3
                continue
            if s[i:i+4] in number_hash:
                answer += number_hash[s[i:i+4]]
                i += 4
                continue
            if s[i:i+5] in number_hash:
                answer += number_hash[s[i:i+5]]
                i += 5
                continue
    return int(answer)