from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(start, stack):
            print(stack)
            # 중복 조건이긴 하나 안전하게 처리하기 위해서 추가
            if len(stack) == len(nums):
                return
            
            result.append(stack[:])

            for i in range(start, len(nums)):
                stack.append(nums[i])
                dfs(i+1, stack)
                stack.pop()
        
        start = 0
        stack = [] # 트리의 깊이
        dfs(start, stack)

        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1, 2, 3]))