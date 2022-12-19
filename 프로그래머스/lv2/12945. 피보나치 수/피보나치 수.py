def solution(n):
    fib = [0 % 1234567, 1 % 1234567]
    for i in range(2, n + 1):
        fib.append((fib[i-2] + fib[i-1]) % 1234567 )
    return fib.pop()

# def fibo(n):
#     # if n == 0:
#     #     return 0
#     # elif n == 1 or n == 2:
#     #     return 1
#     # else:
#     #     return fibo(n-1) + fibo(n-2)