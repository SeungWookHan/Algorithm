def solution(price, money, count):
    total_price = sum([i * price for i in range(1, count+1)])
    return total_price - money if money <= total_price else 0