# work out the divisor closest to the end points then figure out how many are in between
from math import ceil, floor


def solution(A, B, K):
    # write your code in Python 3.6
    start = ceil(A/K)
    end = floor(B/K)
    return end -start + 1