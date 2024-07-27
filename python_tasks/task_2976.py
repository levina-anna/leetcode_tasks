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
        n = len(source)
        if n != len(target):
            return -1

        transform_cost = {}
        for o, c, co in zip(original, changed, cost):
            if (o, c) in transform_cost:
                transform_cost[(o, c)] = min(transform_cost[(o, c)], co)
            else:
                transform_cost[(o, c)] = co

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            s_char = source[i - 1]
            t_char = target[i - 1]
            if s_char == t_char:
                dp[i] = dp[i - 1]
            else:
                min_cost = float('inf')
                if (s_char, t_char) in transform_cost:
                    min_cost = dp[i - 1] + transform_cost[(s_char, t_char)]
                for o, c, co in zip(original, changed, cost):
                    if o == s_char:
                        if (c, t_char) in transform_cost:
                            min_cost = min(min_cost, dp[i - 1] + co + transform_cost[(c, t_char)])
                        if c == t_char:
                            min_cost = min(min_cost, dp[i - 1] + co)
                dp[i] = min_cost

        return dp[n] if dp[n] != float('inf') else -1


sol = Solution()
source = "abc"
target = "bcd"
original = ["a", "b", "c"]
changed = ["b", "c", "d"]
cost = [1, 2, 3]
print(sol.minimumCost(source, target, original, changed, cost))
