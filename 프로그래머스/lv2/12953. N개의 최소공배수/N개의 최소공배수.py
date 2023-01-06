def solution(arr): # 최소공배수 = 두개씩 묶어서 진행
    answer = arr[0]
    for i in range(1, len(arr)):
        gcd = GCD(answer, arr[i])
        LCM = answer * arr[i] / gcd
        answer = LCM
    return answer

def GCD(a, b):
    A = max(a, b)
    B = min(a, b)
    
    while A % B != 0:
        R = A % B
        A = B
        B = R
    return B