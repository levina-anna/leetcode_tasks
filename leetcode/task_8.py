class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert string to a 32-bit signed integer (similar to C/C++'s atoi function).
        """
        s = s.lstrip()
        if not s:
            return 0

        negative = False
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        if negative:
            result = -result

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result

# Example usage
sol = Solution()
example1 = "42"
example2 = "   -42"
example3 = "4193 with words"
example4 = "words and 987"
example5 = "-91283472332"

print(sol.myAtoi(example1)) # Expected output: 42
print(sol.myAtoi(example2)) # Expected output: -42
print(sol.myAtoi(example3)) # Expected output: 4193
print(sol.myAtoi(example4)) # Expected output: 0
print(sol.myAtoi(example5)) # Expected output: -2147483648 (INT_MIN)
