def sumToN(n):
    return n * (n+1) // 2


def solution(A):
    sumN = sumToN(len(A) + 1)
    sumA = sum(A)
    return sumN - sumA


if __name__ == '__main__':
    A = [2,3,1,5]
    result = solution(A)
    result = solution([1])
    print(result)
