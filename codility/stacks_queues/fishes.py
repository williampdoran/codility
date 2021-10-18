def solution(A, B):
    stack = []
    survivors = 0
    for i in range(0, len(A)):
        weight = A[i]
        if B[i] == 1:
            stack.append(weight)
        else:
            weightleft = stack.pop() if stack else -1
            while weightleft != -1 and weightleft < weight:
                weightleft = stack.pop() if stack else -1
            if weightleft == -1:
                survivors += 1
            else:
                stack.append(weightleft)
    return survivors + len(stack)


print(solution([4,3,2,1,5],[0,1,0,0,0]))
