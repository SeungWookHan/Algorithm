# def solution(arr):
#     stack = []
#     answer = [arr[0]]
#     for num in arr:
#         if stack:
#             curr = stack.pop()
#             if curr != num:
#                 answer.append(num)
#         stack.append(num)
#     return answer

def solution(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result