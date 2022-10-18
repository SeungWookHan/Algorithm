def solution(array, commands):
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]


# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))