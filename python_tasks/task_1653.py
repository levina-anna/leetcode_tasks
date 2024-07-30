class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        count_b = 0

        for i in range(n):
            if s[i] == 'a':
                dp[i] = min(dp[i - 1] + 1 if i > 0 else 1, count_b)
            else:
                dp[i] = dp[i - 1] if i > 0 else 0
                count_b += 1

        return dp[-1]
