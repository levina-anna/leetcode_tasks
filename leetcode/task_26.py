class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Индекс для вставки следующего уникального элемента
        insert_pos = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # Найден новый уникальный элемент, перемещаем его в позицию insert_pos
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Возвращаем количество уникальных элементов
        return insert_pos
