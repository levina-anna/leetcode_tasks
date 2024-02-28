class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            is_negative = True
            x = -x
        else:
            is_negative = False

        reversed_x = int(str(x)[::-1])

        if reversed_x > 2 ** 31 - 1:
            return 0

        if is_negative:
            return -reversed_x
        else:
            return reversed_x
