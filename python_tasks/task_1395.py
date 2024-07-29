class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        count = 0
        n = len(rating)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if rating[i] < rating[j] < rating[k]:
                        count += 1

                    if rating[i] > rating[j] > rating[k]:
                        count += 1

        return count
