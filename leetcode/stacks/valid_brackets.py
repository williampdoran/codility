class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char in open_to_close.keys():
                stack.append(char)
            else:
                if stack:
                    brace = stack.pop()
                    if open_to_close.get(brace) == char:
                        pass
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0