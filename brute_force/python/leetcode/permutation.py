from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(path: List[int]):
            print(path)

            if len(path) == len(nums):
                # result.append(deepcopy(path))
                result.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtracking(path)
                    path.pop()

        result = []
        backtracking(path=[])
        return result


if __name__ == '__main__':
    nums = [1, 2]
    solution = Solution()
    ans = solution.permute(nums=nums)
    print(ans)
