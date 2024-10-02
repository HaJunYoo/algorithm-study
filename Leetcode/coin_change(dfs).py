from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(remaining: int) -> int:
            # 기저 조건: 남은 금액이 0이면 성공
            if remaining == 0:
                return 0
            # 기저 조건: 남은 금액이 음수면 불가능
            if remaining < 0:
                return float('inf')

            # 이미 계산된 결과가 있다면 반환
            if remaining in memo:
                return memo[remaining]

            # 모든 동전에 대해 시도
            min_coins = float('inf')
            for coin in coins:
                result = dfs(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            # 결과를 메모에 저장
            memo[remaining] = min_coins
            return min_coins

        memo = {}
        result = dfs(amount)
        return result if result != float('inf') else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1,2,5], 11))  # 예상 출력: 3
    print(solution.coinChange([2], 3))      # 예상 출력: -1
    print(solution.coinChange([1], 0))