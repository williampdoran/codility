def solution(A):
    counts = [0] * (1000000 + 1)
    for i in range(0, len(A)):
        if A[i] > 0:
            counts[A[i]] +=1
    for j in range(1, len(counts)):
        if counts[j] == 0:
            return j

if __name__ == '__main__':
    print(solution([1,3,6,4,1,2]))
    print(solution([1,2,3]))
    print(solution([1,2,7]))
    print(solution([-1, -1]))
    print(solution([-1000000, 1000000]))