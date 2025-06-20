from itertools import permutations
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [elem + 1 for elem in range(n)]

        # self.permute(nums=nums)
        for idx, num in enumerate(permutations(nums), start=1):
            if idx == k:
                temp = [str(e) for e in num]
                ans = ''.join(temp)
                return ans

    def getPermutation2(self, n: int, k: int) -> str:
        print(n, k)
        nums = [elem + 1 for elem in range(n)]

        permutation = ''
        # 0부터 시작해야 한다
        k -= 1
        while n > 0:
            n -= 1
            # 몫 나머지
            index, k = divmod(k, math.factorial(n))
            print(index, k)
            permutation += str(nums[index])
            print(permutation)
            nums.remove(nums[index])

        return permutation

    @staticmethod
    def permute(nums):
        def backtracking(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()

        ans = []
        backtracking([])
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    n = 3
    k = 3
    # ans = solution.permute(nums=nums)
    ans = solution.getPermutation2(n=n, k=k)
    print(ans)
