def solution(S):
    stack = []
    open_close = {'{' : '}', '[':']', '(':')'}
    for car in S:
        if car in open_close.keys():
            stack.append(car)
        if car in open_close.values():
            if not stack or open_close[stack.pop()] != car:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution("{[()()]}"))
print(solution("([)()]"))