from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()

        result = []
        backtracking(1, [])
        return result
