def palindrome(s: str, start, end):
    if is_palindrome(s[start:end+1]):
        return -1
    else:
        if s[start] == s[end]:
            start +=1
            end -= 1
            return palindrome(s, start, end)
        if is_palindrome(s[start: end]):
            return end
        elif is_palindrome(s[start +1: end+1]):
            return start
        else:
            return -1

def is_palindrome(s: str):
    if len(s) <=1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    elif s[0] != s[-1]:
        return False

def palindromeIndex(s):
    start = 0
    end = len(s) -1
    return palindrome(s, start, end)

assert 3 == palindromeIndex('aaab')
assert 0 == palindromeIndex('baa')
assert -1 == palindromeIndex('aaa')
assert -1 == palindromeIndex('abba')
assert 1 == palindromeIndex('quyjjdcgsvvsgcdjjyq')
