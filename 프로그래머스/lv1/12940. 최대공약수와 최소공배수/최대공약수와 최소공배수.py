def GCD(n, m):
    if(n % m == 0 or m == 1):
        return m
    return GCD(m, n % m)

def LCM(n, m, gcd):
    return n * m // gcd

def solution(n, m):
    if n < m:
        n, m = m, n
    gcd = GCD(n, m)
    lcm = LCM(n, m, gcd)
    return [gcd, lcm]