class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort()

        first, last = strs[0], strs[-1]
        common_prefix = []

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common_prefix.append(first[i])
            else:
                break

        return ''.join(common_prefix)


# Example usage
solution = Solution()
example_strs = ["flower", "flow", "flight"]
longest_common_prefix = solution.longestCommonPrefix(example_strs)
longest_common_prefix
