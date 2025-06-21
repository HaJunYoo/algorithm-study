import sys
sys.stdin = open('in5.txt', 'r')

if __name__ == "__main__":

    n = int(input())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    print(coins)

    min_diff = 128000000

    def dfs(idx, sum_a, sum_b, sum_c):
        global min_diff

        if idx == n:
            # 세 사람의 총액은 서로 달라야 합니다.
            if sum_a != sum_b and sum_b != sum_c and sum_a != sum_c:
                # 총액이 가장 큰
                # 사람과 가장 작은 사람의 차가 최소
                max_sum = max(sum_a, sum_b, sum_c)
                min_sum = min(sum_a, sum_b, sum_c)
                diff = abs(max_sum-min_sum)
                # print(diff)
                # print(f'{sum_a} {sum_b} {sum_c} = {diff}')
                min_diff = min(diff, min_diff)
            return

        else:
            # print(coins[idx])
            coin = coins[idx]
            dfs(idx+1, sum_a + coin, sum_b, sum_c)
            dfs(idx+1, sum_a, sum_b + coin, sum_c)
            dfs(idx+1, sum_a, sum_b, sum_c + coin)


    # idx, a, b, c
    dfs(0, 0, 0, 0)
    print('......')
    print(min_diff)

# A B C
# humans = [[],[],[]]

# def sum_coin():
#     sum_list = []
#     for human in humans:
#         sum_list.append(sum(human))

#     diff = abs(max(sum_list) - min(sum_list))
#     return diff

'''
7
8
9
11
12
23
15
17
'''
'''
32 34 29 = 5
32 32 31 = 1
'''