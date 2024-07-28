from heapq import heappush, heappop
from collections import defaultdict, deque


class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        # Построение графа
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Массив для хранения двух минимальных времен для достижения каждого узла
        min_time = [[float('inf'), float('inf')] for _ in range(n + 1)]
        min_time[1][0] = 0

        # Приоритетная очередь для алгоритма Дейкстры
        pq = [(0, 1)]  # (текущее время, текущий узел)

        while pq:
            current_time, node = heappop(pq)

            for neighbor in graph[node]:
                # Расчет времени с учетом светофоров
                t = current_time
                if (t // change) % 2 == 1:
                    t = (t // change + 1) * change
                new_time = t + time

                if new_time < min_time[neighbor][0]:
                    min_time[neighbor][1] = min_time[neighbor][0]
                    min_time[neighbor][0] = new_time
                    heappush(pq, (new_time, neighbor))
                elif min_time[neighbor][0] < new_time < min_time[neighbor][1]:
                    min_time[neighbor][1] = new_time
                    heappush(pq, (new_time, neighbor))

        # Возвращаем второе минимальное время для достижения узла n
        return min_time[n][1]


sol = Solution()
n = 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time = 3
change = 5
print(sol.secondMinimum(n, edges, time, change))  # Ожидаемый результат: 13
