class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transposed = []

        for i in range(len(matrix[0])):

            transposed_row = []

            for row in matrix:
                transposed_row.append(row[i])

            transposed.append(transposed_row)

        return transposed

# Instantiate the class
solution = Solution()

# Test cases
test_cases = [
    ([[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]]),
    ([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]),
    ([[1]], [[1]])
]

# Test the method
for matrix, expected in test_cases:
    result = solution.transpose(matrix)
    assert result == expected, f"Test failed for input {matrix}. Expected {expected}, got {result}"

print("All tests passed.")