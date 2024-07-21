from collections import defaultdict, deque


class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """

        def topological_sort(n, conditions):
            graph = defaultdict(list)
            in_degree = [0] * (n + 1)

            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1

            queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
            top_order = []

            while queue:
                node = queue.popleft()
                top_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if len(top_order) == n:
                return top_order
            else:
                return []

        row_order = topological_sort(k, rowConditions)
        col_order = topological_sort(k, colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {val: idx for idx, val in enumerate(row_order)}
        col_pos = {val: idx for idx, val in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num

        return matrix


solution = Solution()
k = 3
rowConditions = [[1, 2], [2, 3]]
colConditions = [[2, 1], [3, 2]]

print(solution.buildMatrix(k, rowConditions, colConditions))
