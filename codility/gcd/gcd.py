def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)


def lcm(a, b):
    return (a * b)/gcd(a,b)


def solution(n, m):
    return  lcm(n,m)//m

print(gcd(5, 15))
print(lcm(5, 15))
print(gcd(4, 10))
print(lcm(4, 10))
print(solution(10, 4))