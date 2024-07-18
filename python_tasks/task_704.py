class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


sol = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 9
expected_result = 4
assert sol.search(nums, target) == expected_result, f"Test failed for target {target} in {nums}"


nums = [-1, 0, 3, 5, 9, 12]
target = 2
expected_result = -1
assert sol.search(nums, target) == expected_result, f"Test failed for target {target} in {nums}"

print("Good!")
