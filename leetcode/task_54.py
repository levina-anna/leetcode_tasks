class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            # Add the first row to result
            res += matrix.pop(0)
            # Add the last element of each remaining row
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            # Add the last row to result in reverse order
            if matrix:
                res += matrix.pop()[::-1]
            # Add the first element of each remaining row in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

# Test the solution
sol = Solution()
mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
sol.spiralOrder(mat)
