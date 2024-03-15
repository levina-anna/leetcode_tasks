class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()  # Сортировка массива для двойного указателя
        closest = float('inf')  # Инициализация самой близкой суммы как "бесконечность"

        for i in range(len(nums) - 2):  # Перебираем каждый элемент как начальный элемент тройки
            left, right = i + 1, len(nums) - 1  # Инициализация указателей

            while left < right:  # Пока левый указатель меньше правого
                current_sum = nums[i] + nums[left] + nums[right]  # Текущая сумма трех элементов

                # Обновляем closest, если текущая сумма ближе к цели, чем предыдущая closest
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # Если сумма меньше цели, сдвигаем левый указатель
                if current_sum < target:
                    left += 1
                # Если сумма больше цели, сдвигаем правый указатель
                elif current_sum > target:
                    right -= 1
                else:
                    # Если сумма равна цели, то это наилучший возможный результат
                    return current_sum

        return closest  # Возвращаем самую близкую сумму
