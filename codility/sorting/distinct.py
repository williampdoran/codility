def solution(A):
    n = len(A)
    A.sort()
    result = 1
    for i in range(1, n):
        if A[i] != A[i-1]:
            result += 1
    return result
