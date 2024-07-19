class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_row = {min(row) for row in matrix}
        max_col = {max(col) for col in zip(*matrix)}
        return list(min_row & max_col)
