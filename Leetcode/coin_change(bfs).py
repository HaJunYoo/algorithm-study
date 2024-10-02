from typing import List
from collections import deque


def coinChange(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    queue = deque([])
    visited = set()

    # 현재 금액, 사용한 코인 개수
    queue.append((0, 0))
    # 현재 금액을 visited에 등록
    visited.add(0)

    while queue:
        current_amount, coin_used = queue.popleft()

        for coin in coins:
            next_amount = current_amount + coin

            if next_amount == amount:
                return coin_used + 1

            if next_amount < amount and next_amount not in visited:
                queue.append((next_amount, coin_used + 1))
                visited.add(next_amount)

    return -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11

    ans = coinChange(coins, amount)
    print(ans)
