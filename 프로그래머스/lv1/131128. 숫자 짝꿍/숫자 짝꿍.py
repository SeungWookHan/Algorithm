def solution(X: str, Y: str) -> str:
    list_X = list(X)
    list_Y = list(Y)
    # common = list(set(list1).intersection(list2)) # 오답
    common = []
    for i in (set(X)&set(Y)) : # 공통 숫자 찾기, 리스트화
        for j in range(min(X.count(i), Y.count(i))) :
            common.append(i)
    if len(common) == 0:
        return "-1"
    
    common.sort(reverse=True)
    if common[0] == "0":
        return "0"
    
    return "".join(common)