class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        total_sum = 0
        for i in range(n):
            total_sum += mat[i][i]
            total_sum += mat[i][n - 1 - i]

        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]

        return total_sum
