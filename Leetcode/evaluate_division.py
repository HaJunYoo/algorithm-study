from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1
            if x == y:
                return 1

            visited.add(x)

            for ad in graph[x]:
                if ad not in visited:
                    result = dfs(ad, y, visited)
                    if result != -1:
                        return result * graph[x][ad]

            return -1

        result = []
        for x, y in queries:
            res = dfs(x, y, set())
            result.append(res)

        return result


if __name__ == '__main__':
    s = Solution()
    answer = s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    print(answer)
