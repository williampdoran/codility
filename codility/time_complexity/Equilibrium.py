def solution(A):
    total = sum(A)
    sumleft = A[0]
    sumright = total - sumleft
    current_lowest = abs(sumleft - sumright)
    if(len(A) == 2):
        return current_lowest
    else:
        for p in range(1, len(A)-1):
            sumleft = A[p] + sumleft
            sumright = sumright - A[p]
            diff = abs(sumleft - sumright)
            print(f'{p} {current_lowest} {sumleft} {sumright} {diff}')
            if diff < current_lowest:
                current_lowest = diff
    return current_lowest

if __name__ == '__main__':
    A = [None] * 5
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 4
    A[4] = 3
    print(solution(A))
    print(solution([-1000, 1000]))
    print(solution([-10, -20, -30, -40, 100])) #should be 20


