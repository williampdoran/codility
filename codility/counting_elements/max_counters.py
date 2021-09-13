def solution(n, A):
    counters = [0] * n
    maximun = 0
    start_line = 0
    for i in range(0, len(A)):
        if A[i] == n + 1:
            start_line = maximun
        else:
            if counters[A[i] -1] < start_line:
                counters[A[i] -1] = start_line + 1
            else:
                counters[A[i] -1] += 1
            maximun = max(maximun, counters[A[i] -1])
        # print(i, A[i], counters, maximun, start_line)

    for i in range(0, len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line

    return counters

if __name__ == '__main__':
    print(solution(5,[3,4,4,6,1,4,4]))