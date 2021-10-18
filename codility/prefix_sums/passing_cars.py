# the trick here is to count the suffix sums where car is equal to zero

def solution(N):
    count = 0
    suffix_sums = [0] * (len(N) + 1)
    for i in range(len(N) -1, -1, -1):
        suffix_sums[i] = N[i] + suffix_sums[i + 1]
        if(N[i] == 0):
            count += suffix_sums[i]
        if count > 1000000000:
            return  -1
    return count

N = [0,1,0,1,1]
print(solution(N))
