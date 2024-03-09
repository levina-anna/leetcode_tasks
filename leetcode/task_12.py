class Solution:
    def intToRoman(self, num: int) -> str:
        # Сопоставление римских чисел с их десятичными эквивалентами
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        # Результат будет собираться здесь
        roman_numerals = ""

        # Для каждого римского числа в списке
        for value, numeral in values:
            # Определяем, сколько раз это римское число укладывается в num
            count = num // value
            # Если укладывается хотя бы один раз
            if count:
                # Добавляем соответствующее римское число в результат count раз
                roman_numerals += numeral * count
                # Уменьшаем num на общую величину добавленных римских чисел
                num -= value * count

        return roman_numerals


# Создание экземпляра класса Solution
solution = Solution()

# Вызов метода intToRoman для экземпляра класса, передавая число как аргумент
result = solution.intToRoman(18)

# Вывод результата
print(result)  # Ожидается вывод "XVIII"

