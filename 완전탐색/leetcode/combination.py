from typing import List
from copy import deepcopy

from copy import deepcopy
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(start: int, path: List[int]):

            if len(path) == k:
                result.append(deepcopy(path))
                return

            for i in range(start, n + 1):
                path.append(i)
                backtracking(start=i + 1, path=path)
                path.pop()

        result = []
        backtracking(start=1, path=[])
        return result


if __name__ == '__main__':
    n = 4
    k = 2
    ans = combine(n=n, k=k)
    print(ans)
