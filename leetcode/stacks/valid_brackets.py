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

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {'{':'}', '(':')','[':']'}
        for c in s:
            if c in bracket_map.keys():
                stack.append(c)
            else:
                if stack:
                    opening_brace = stack.pop()
                    if bracket_map.get(opening_brace) == c:
                        pass
                    else:
                        return False
                else:
                    return False
        return len(stack) ==0

    def isValidShitQuick(self, s):
        queue = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in close_to_open.values():
                queue.append(char)
            elif len(queue) > 0 and close_to_open[char] == queue[-1]:
                queue.pop()
            else:
                return False
        answer = "YES" if len(queue) == 0 else "NO"
        return len(queue) == 0

assert Solution().isValidShitQuick('()') == True

