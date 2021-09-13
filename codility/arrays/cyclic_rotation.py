def solution(A, K):
    n = len(A)
    B = [None] * len(A)
    if K == 0:
        return A
    else:
        for i in range(0, len(A)):
            B[(i + K) % n] = A[i]
        return B


if __name__ == '__main__':
    A = [1,2,3,4]
    print(solution([1,2,3,4], 4))
    print(solution([3, 8, 9, 7, 6], 3))
    print(solution([5, -1000], 1))
    print(solution([], 4))
    print(solution([1,2,3,4], 0))
