def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0 , len(score) - len(score) % m, m):
        box = score[i:i+m]
        answer += box[m-1] * m
        
        # if len(box) == m:
        #     answer += box[m-1] * m
            
    # while len(score) >= m:
    #     answer += score[:m][m-1] * m
    #     score = score[m:]
    return answer