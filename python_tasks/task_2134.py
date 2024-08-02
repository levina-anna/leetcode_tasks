class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_ones = nums.count(1)

        if total_ones == 0 or total_ones == n:
            return 0

        double_nums = nums + nums

        min_swaps = float('inf')
        current_zeros = 0

        for i in range(total_ones):
            if double_nums[i] == 0:
                current_zeros += 1

        min_swaps = current_zeros

        for i in range(total_ones, 2 * n):
            if double_nums[i] == 0:
                current_zeros += 1
            if double_nums[i - total_ones] == 0:
                current_zeros -= 1

            min_swaps = min(min_swaps, current_zeros)

        return min_swaps
