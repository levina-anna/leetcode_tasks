class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row, step = 0, -1

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                step = -step

            current_row += step

        return ''.join(rows)
