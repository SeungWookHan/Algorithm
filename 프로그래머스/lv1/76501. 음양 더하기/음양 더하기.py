def change_to_negative(x, y):
    if y == False:
        return -x
    return x

def solution(absolutes, signs):
    return sum(list(map(change_to_negative, absolutes, signs)))