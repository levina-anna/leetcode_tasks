class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        step = 0
        x, y = rStart, cStart

        while len(result) < rows * cols:
            if step % 2 == 0:
                step_len = step // 2 + 1
            else:
                step_len = (step + 1) // 2

            dx, dy = directions[step % 4]
            for _ in range(step_len):
                if 0 <= x < rows and 0 <= y < cols:
                    result.append([x, y])
                x += dx
                y += dy

            step += 1

        return result
