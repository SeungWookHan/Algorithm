def solution(brown, yellow):
    sum = brown + yellow
    x, y = 0, 0
    for i in range(1, sum + 1):
        x = i
        y = sum // x
         # 위아래 각각 1줄씩 (총 2줄), 양옆 각각 1줄씩 (총 2줄) 빼면 노란 격자의 가로 세로 길이
        # 그리고 (가로)*(세로)가 yellow 격자의 개수와 일치하는지 확인
        if x * y == sum and x >= y:
            check = sum - (x*2 + (y-2)*2)
            if check == yellow:
                break
    return [x, y]