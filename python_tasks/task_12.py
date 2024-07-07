class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman_numerals = ""

        for value, numeral in values:
            count = num // value
            if count:
                roman_numerals += numeral * count
                num -= value * count

        return roman_numerals


solution = Solution()
result = solution.intToRoman(18)
print(result)
