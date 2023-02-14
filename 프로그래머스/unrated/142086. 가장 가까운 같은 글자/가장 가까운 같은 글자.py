def solution(s):
    hash = {}
    answer = []
    for i in range(len(s)):
        word = s[i]
        if hash.get(word, None) == None:
            hash[word] = i
            answer.append(-1)
        else:
            answer.append(i - hash[word])
            hash[word] = i
    return answer