from typing import List


# the key to this one, is that you only need to track the differences at the start
#and end interval. Then do a max slice sum

def max_sum(A):
    max_ending_here, max_so_far = 0, 0
    for i in range(0, len(A)):
        max_ending_here = max(0, max_ending_here + A[i])
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far

def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for query in queries:
        start, end, value = query
        arr[start-1] += value
        arr[end] -= value
    return max_sum(arr)

n=5
queries=[[1,2,100],[2,5,100],[3,4,100]]
result = arrayManipulation(n, queries)
assert result == 200