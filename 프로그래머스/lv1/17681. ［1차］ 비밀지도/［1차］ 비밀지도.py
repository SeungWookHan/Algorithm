def solution(n, arr1, arr2):
    # print([(bin(arr1_ | arr2_)[2:]) for arr1_, arr2_ in zip(arr1, arr2)])
    answer = [(bin(arr1_ | arr2_)[2:]).zfill(n).replace("1", "#").replace("0", " ") for arr1_, arr2_ in zip(arr1, arr2)]
    return answer