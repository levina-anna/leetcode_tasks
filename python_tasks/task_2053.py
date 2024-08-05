class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        from collections import Counter
        frequency = Counter(arr)

        distinct_count = 0

        for string in arr:
            if frequency[string] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return string

        return ""


solution = Solution()
arr = ["a", "b", "a", "c", "b", "d"]
k = 2
print(solution.kthDistinct(arr, k))
