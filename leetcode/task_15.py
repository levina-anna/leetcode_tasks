class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):  # Последние два элемента не нужно рассматривать как начальные точки
            if i > 0 and nums[i] == nums[i - 1]:  # Пропустить дубликаты
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # Пропустить дубликаты
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # Пропустить дубликаты
                        right -= 1
                    left += 1
                    right -= 1

        return result