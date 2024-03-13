class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Если needle — пустая строка, возвращаем 0, как указано в условии задачи
        if not needle:
            return 0

        # Проверяем каждую подстроку haystack, которая имеет такую же длину, как needle
        for i in range(len(haystack) - len(needle) + 1):
            # Если подстрока совпадает с needle, возвращаем её начальный индекс
            if haystack[i:i + len(needle)] == needle:
                return i

        # Если needle не найден в haystack, возвращаем -1
        return -1
