class Solution:
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        total_sum = 0
        for i in range(n):
            total_sum += mat[i][i]  # Главная диагональ
            total_sum += mat[i][n - 1 - i]  # Побочная диагональ

        if n % 2 == 1:  # Если размер матрицы нечетный, вычесть центральный элемент, так как он был добавлен дважды
            total_sum -= mat[n // 2][n // 2]

        return total_sum


# Test the solution
sol = Solution()
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sol.diagonalSum(mat))
