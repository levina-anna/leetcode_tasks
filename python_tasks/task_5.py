class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) == 0:
            return ""

        maxPalindrome = ""
        for i in range(len(s)):
            palindrome1 = expandAroundCenter(i, i)
            if len(palindrome1) > len(maxPalindrome):
                maxPalindrome = palindrome1

            palindrome2 = expandAroundCenter(i, i + 1)
            if len(palindrome2) > len(maxPalindrome):
                maxPalindrome = palindrome2

        return maxPalindrome
