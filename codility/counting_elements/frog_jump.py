def solution(X, A):
    steps = [0] * X
    covered_steps = 0
    for i in range(0, len(A)):
        if(steps[A[i]-1] == 0):
            covered_steps +=1
            steps[A[i]-1] += 1
        if covered_steps == X:
            return i
    return -1

if __name__ == '__main__':
    print(solution(5, [1,3,1,4,2,3,5,4]))