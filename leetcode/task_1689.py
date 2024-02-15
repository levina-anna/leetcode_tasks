class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return max(int(digit) for digit in n)


result = Solution().minPartitions(str(32))
print(result)
