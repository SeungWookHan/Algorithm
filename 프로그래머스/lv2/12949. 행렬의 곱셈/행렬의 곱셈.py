def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        tmp = [0] * len(arr2[0])
        for j in range(len(arr1[0])):
            for k in range(len(arr2[0])):
                tmp[k] += arr1[i][j] * arr2[j][k]
        answer[i] = tmp
    return answer