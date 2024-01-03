from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    # 재귀를 이용하기 때문에 시간복잡도가 더 높다. -> 통과 안됨 (Time Limit Exceeded)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        def backtracking(start: int):
            if len(ans) == 2:
                if nums[ans[0]] + nums[ans[1]] == target:
                    return ans
                return False

            for i in range(start, len(nums)):
                ans.append(i)
                if backtracking(start=i + 1):
                    return ans
                ans.pop()

        return backtracking(start=0)
