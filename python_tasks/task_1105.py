class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        dp = [0] * (len(books) + 1)
        dp[0] = 0

        for i in range(1, len(books) + 1):
            width = 0
            height = 0
            dp[i] = float('inf')

            for j in range(i - 1, -1, -1):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)

        return dp[len(books)]