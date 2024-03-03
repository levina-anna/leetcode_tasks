class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_pair = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in bracket_pair.values():
                stack.append(char)
            elif char in bracket_pair.keys():
                if stack == [] or bracket_pair[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


sol = Solution()
print(sol.is_valid("()"))