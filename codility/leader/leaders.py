def slowLeader(A):
    n = len(A)
    leader = -1
    for i in range(0, n):
        candidate = A[i]
        count = 0
        for j in range(0, n):
            if candidate == A[j]:
                count += 1
        if count > n//2:
            leader = candidate
    return leader


def sortedLeader(A):
    n = len(A)
    A.sort()
    candidate = A[n//2]
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count += 1
    if count > n //2:
        return candidate
    else:
        return -1

def goldenLeader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size ==0):
            size += 1
            value = A[k] #top of stack
        else:
            if (value != A[k]): #if values on stack are different, reduce
                size -= 1
            else:
                size += 1
    candidate = -1
    if size >0:
        candidate = value
    count = 0
    index = -1
    for k in range(n):
        if (A[k] == candidate):
            index = k
            count +=1
    if count > n//2:
        return index
    else:
        return -1

def goldenStackLeader(A):
    n = len(A)
    stack = []
    for k in range(n):
        if stack and A[k] != stack.pop():
            continue
        else:
            stack.append(A[k])
            stack.append(A[k])
    candidate = -1
    if len(stack) >0:
        candidate = stack.pop()
    count = 0
    index = -1
    for k in range(n):
        if (A[k] == candidate):
            index = k
            count +=1
    if count > n//2:
        return index
    else:
        return -1

# print(slowLeader([4,6,6,6,6,8,8]))
# print(sortedLeader([4,6,6,6,8,8,8]))
print(goldenLeader([3, 4, 3, 2, 3, -1, 3, 3]))
# print(goldenStackLeader([4,6,6,6,8,6,8]))