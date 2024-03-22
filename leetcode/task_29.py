class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Определяем знак результата
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Работаем с абсолютными значениями, чтобы упростить логику
        dividend, divisor = abs(dividend), abs(divisor)

        # Инициализируем результат
        quotient = 0

        # Пока дивиденд больше или равен делителю
        while dividend >= divisor:
            # Начинаем с самой степени двойки
            temp, i = divisor, 1

            # Удваиваем делитель, пока он меньше дивиденда
            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1
                temp <<= 1

        # Применяем знак к результату
        quotient *= sign

        # Обрабатываем переполнение
        return min(max(-2 ** 31, quotient), 2 ** 31 - 1)