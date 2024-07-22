class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        sorted_people = sorted(zip(heights, names), reverse=True)
        sorted_names = [name for height, name in sorted_people]
        return sorted_names


solution = Solution()
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]

print(solution.sortPeople(names, heights))
