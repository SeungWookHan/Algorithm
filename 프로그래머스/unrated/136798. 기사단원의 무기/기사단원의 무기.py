def solution(number, limit, power):
    answer = []
    
    for i in range(1, number+1):
        num_of_divisor = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                num_of_divisor += 1
                if j ** 2 != i:
                    num_of_divisor += 1
        answer.append(num_of_divisor)
    return sum([x if x <= limit else power for x in answer])