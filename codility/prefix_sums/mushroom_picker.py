def prefix_sums(A):
    sums = [0] * (len(A) + 1)
    for i in range(1, len(A)+1):
        sums[i] = sums[i -1] + A[i -1]
    return sums

def count_total(P, x, y):
    return P[y +1] - P[x]


