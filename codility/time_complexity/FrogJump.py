def solution(X, Y, D):
    journey = (Y - X)
    if journey % D == 0:
        return journey // D
    else:
        return journey // D + 1

if __name__ == '__main__':
    X = 10
    Y = 85
    D = 30
    print(solution(X, Y, D))