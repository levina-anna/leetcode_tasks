class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        import heapq

        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)

        subarray_sums.sort()
        result = sum(subarray_sums[left - 1:right])

        return result
