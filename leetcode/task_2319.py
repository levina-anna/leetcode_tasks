class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:  # На диагоналях
                    if grid[i][j] == 0:
                        return False
                else:  # Вне диагоналей
                    if grid[i][j] != 0:
                        return False
        return True


# Пример тестирования решения
sol = Solution()
grid = [
    [2, 0, 0, 1],
    [0, 3, 1, 0],
    [0, 5, 2, 0],
    [4, 0, 0, 2]
]

print(sol.checkXMatrix(grid))
