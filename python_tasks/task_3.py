class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length


solution = Solution()

test_cases = ["abcabcbb", "bbbbb", "pwwkew", ""]
results = [solution.lengthOfLongestSubstring(test_case) for test_case in test_cases]
print(results)
