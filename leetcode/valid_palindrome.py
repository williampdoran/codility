import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^\w]', '', s).replace('_','')
        if len(s) <=1:
            return True
        print(s)
        start, end = 0, len(s)-1
        while end > start:
            print(start, end, f"{s[start]}", f"{s[end]}")
            if s[start] != s[end]:
                return False
            end = end -1
            start = start + 1
        return True

    def isPalindromeRecursive(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def palindromeHelper(s, start, end):
            print(s, start, end, f"{s[start]}", f"{s[end]}")
            if len(s) <=1:
                return True
            if end <= start:
                return True
            elif s[start] != s[end]:
                return False
            else:
                return palindromeHelper(s, start +1, end -1)
            return True
        s = s.lower()
        s = re.sub(r'[^\w]', '', s).replace('_','')
        start, end = 0, len(s) - 1
        return palindromeHelper(s, start, end)

test_string = "A man, a plan, a canal: Panama"
assert Solution().isPalindromeRecursive(test_string) == True
assert Solution().isPalindromeRecursive("ab_a") == True
assert Solution().isPalindromeRecursive("abba") == True
assert Solution().isPalindromeRecursive("abcda") == False


# assert Solution().isPalindrome(test_string) == True
# assert Solution().isPalindrome("ab_a") == True