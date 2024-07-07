class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]

        carry, i = 1, 0
        while carry:
            if i < len(digits):
                if digits[i] < 9:
                    digits[i] += carry
                    carry = 0
                else:
                    digits[i] = 0
            else:
                digits.append(carry)
                carry = 0
            i += 1

        return digits[::-1]


solution = Solution()
result = solution.plusOne([9, 9, 9])
print(result)
