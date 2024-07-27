class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        n = 26
        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for i in range(len(original)):
            from_char = ord(original[i]) - ord('a')
            to_char = ord(changed[i]) - ord('a')
            dist[from_char][to_char] = min(dist[from_char][to_char], cost[i])

        for k in range(n):
            for i in range(n):
                if dist[i][k] != float('inf'):
                    for j in range(n):
                        if dist[k][j] != float('inf'):
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        min_cost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            a = ord(source[i]) - ord('a')
            b = ord(target[i]) - ord('a')
            if dist[a][b] == float('inf'):
                return -1
            else:
                min_cost += dist[a][b]

        return min_cost