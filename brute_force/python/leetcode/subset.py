from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start: int, stack: List[int]):
            print(stack)
            result.append(stack[:])

            for i in range(start, len(nums)):
                stack.append(nums[i])
                dfs(i + 1, stack)
                stack.pop()

        start = 0
        result = []
        stack = []
        dfs(start, stack)

        return result
