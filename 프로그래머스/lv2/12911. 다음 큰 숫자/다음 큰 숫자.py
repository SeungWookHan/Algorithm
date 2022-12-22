def solution(n):
    count = bin(n).count("1")
    while True:
        n = n + 1
        b = bin(n)
        if b[2:].count("1") == count:
            break
    return n