# def solution(n):
#     count = 0
#     sieve = [True] * (n + 1) # 채 초기화
    
#     for i in range(2, int(n ** 0.5) + 1):
#         if sieve[i] == True:
#             for j in range(i + i, n + 1, i):
#                 sieve[j] = False
#     for i in range(2, n + 1):
#         if sieve[i] == True:
#             count += 1
#     return count

def solution(n):
    answer = set(range(2, n+1))
    
    for i in range(2, int(n ** 0.5) + 1):
        if i in answer:
            answer -= set(range(i + i, n + 1, i))
    return len(answer)