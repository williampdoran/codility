def solution(A):
    current = 0
    for i in A:
        current = current ^ i
    return current

if __name__ == '__main__':
    print(solution([9,3,9,5,5,3,6,6, 7]))