def max_sum(A):
    max_ending_here, max_so_far = 0, 0
    for i in range(0, len(A)):
        max_ending_here = max(0, max_ending_here + A[i])
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far

print(max_sum([5,-7,3,5,-2,4,-1]))

def solution(A):
    if len(A) < 2: return 0
    max_to_here, max_profit = A[-1], 0
    for i in range(len(A)-2, -1, -1):
        max_to_here = max(max_to_here, A[i])
        max_profit = max(max_to_here - A[i], max_profit)
    return max_profit

def solution2(A):
    if len(A) < 2: return 0
    profits = [0] * (len(A) -1)
    for i in range(0, len(A) -1):
        profits[i] = A[i+1] - A[i]
    return max_sum(profits)


print(solution([23171,21011,21123,21366,21013,21367]))
print(solution2([23171,21011,21123,21366,21013,21367]))