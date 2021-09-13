def solution(A):
    n = len(A)
    counter = [0] * n
    for e in A:
        # print(e, counter)
        if e > n:
            return 0
        if counter[e-1] > 0:
            return 0
        else:
            counter[e-1] = 1
    # print(counter)
    return 1

# print("result", solution([4,1,3,2]))
# print("result", solution([4,1,3]))
# print("result", solution([1,2]))
# print("result", solution([1,3]))
# print("result", solution([2]))
print("result", solution([1]))
# "result",