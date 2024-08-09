class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def isMagic(i, j):
            s = set()
            for x in range(3):
                for y in range(3):
                    s.add(grid[i + x][j + y])
            if s != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False

            if grid[i][j] + grid[i][j + 1] + grid[i][j + 2] != 15:
                return False
            if grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] != 15:
                return False
            if grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] != 15:
                return False
            if grid[i][j] + grid[i + 1][j] + grid[i + 2][j] != 15:
                return False
            if grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] != 15:
                return False
            if grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] != 15:
                return False
            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != 15:
                return False
            if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != 15:
                return False

            return True

        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                if grid[i + 1][j + 1] == 5 and isMagic(i, j):
                    count += 1

        return count
